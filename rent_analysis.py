#!/usr/bin/env python3
"""
Rent analysis module for Section 8 Housing Data Analysis
This module analyzes rent distribution and affordability metrics
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_rent_distribution(df):
    """
    Analyze and visualize rent distribution across different bedroom sizes
    
    Args:
        df (pd.DataFrame): The preprocessed housing data
    """
    # Create a figure for rent distribution by bedroom size
    plt.figure(figsize=(12, 8))
    
    # Create box plots for each bedroom size
    bedroom_cols = ['rent_50_0', 'rent_50_1', 'rent_50_2', 'rent_50_3', 'rent_50_4']
    bedroom_labels = ['Studio', '1-Bedroom', '2-Bedroom', '3-Bedroom', '4-Bedroom']
    
    # Convert data to format suitable for boxplot
    plot_data = []
    for col in bedroom_cols:
        plot_data.append(df[col])
    
    # Create boxplot
    plt.boxplot(plot_data, patch_artist=True, labels=bedroom_labels)
    plt.title('Distribution of Fair Market Rent by Bedroom Size in Pacific Northwest (2023)')
    plt.ylabel('Monthly Rent ($)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Save the figure
    plt.tight_layout()
    plt.savefig('visualizations/rent_distribution_by_bedroom.png')
    plt.close()
    
    # Create a bar chart showing average rent by state
    plt.figure(figsize=(10, 6))
    state_avg_rent = df.groupby('state')['avg_rent'].mean().sort_values(ascending=False)
    
    sns.barplot(x=state_avg_rent.index, y=state_avg_rent.values)
    plt.title('Average Rent by State in Pacific Northwest (2023)')
    plt.ylabel('Average Monthly Rent ($)')
    plt.xlabel('State')
    
    # Add value labels on bars
    for i, v in enumerate(state_avg_rent.values):
        plt.text(i, v + 20, f'${int(v)}', ha='center')
    
    plt.tight_layout()
    plt.savefig('visualizations/average_rent_by_state.png')
    plt.close()

def rent_to_income_ratio(df):
    """
    Analyze and visualize the relationship between rent and income
    
    Args:
        df (pd.DataFrame): The preprocessed housing data
    """
    # Create scatter plot of median income vs median rent
    plt.figure(figsize=(12, 8))
    
    # Create scatter plot with color based on state
    states = df['state'].unique()
    colors = plt.cm.tab10(np.linspace(0, 1, len(states)))
    
    for i, state in enumerate(states):
        state_data = df[df['state'] == state]
        plt.scatter(
            state_data['median_incomeE'], 
            state_data['median_rentE'],
            color=colors[i],
            alpha=0.7,
            label=state,
            s=state_data['total_popE'] / 5000  # Size based on population
        )
    
    # Add a trend line
    x = df['median_incomeE']
    y = df['median_rentE']
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), "r--", alpha=0.8)
    
    plt.title('Relationship Between Median Income and Median Rent')
    plt.xlabel('Median Annual Income ($)')
    plt.ylabel('Median Monthly Rent ($)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(title='State')
    
    plt.tight_layout()
    plt.savefig('visualizations/income_vs_rent.png')
    plt.close()
    
    # Create histogram of rent burden percentage
    plt.figure(figsize=(12, 8))
    
    # Remove outliers for better visualization
    rent_burden = df['rent_burden'].copy()
    rent_burden = rent_burden[rent_burden < rent_burden.quantile(0.95)]
    
    sns.histplot(rent_burden, bins=20, kde=True)
    plt.axvline(x=30, color='r', linestyle='--', label='30% Threshold')
    plt.title('Distribution of Rent Burden (Monthly Rent as % of Monthly Income)')
    plt.xlabel('Rent Burden (%)')
    plt.ylabel('Number of Counties')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('visualizations/rent_burden_distribution.png')
    plt.close()
