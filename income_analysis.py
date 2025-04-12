#!/usr/bin/env python3
"""
Income analysis module for Section 8 Housing Data Analysis
This module analyzes income, poverty, and their relationship to housing
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_income_poverty_relation(df):
    """
    Analyze and visualize relationships between income, poverty, and housing
    
    Args:
        df (pd.DataFrame): The preprocessed housing data
    """
    # Create scatter plot of poverty rate vs median income
    plt.figure(figsize=(12, 8))
    
    # Create scatter plot with color based on state
    states = df['state'].unique()
    colors = plt.cm.tab10(np.linspace(0, 1, len(states)))
    
    for i, state in enumerate(states):
        state_data = df[df['state'] == state]
        plt.scatter(
            state_data['median_incomeE'], 
            state_data['poverty_rate'],
            color=colors[i],
            alpha=0.7,
            label=state,
            s=state_data['total_popE'] / 5000  # Size based on population
        )
    
    # Add a trend line
    x = df['median_incomeE']
    y = df['poverty_rate']
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), "r--", alpha=0.8)
    
    plt.title('Relationship Between Median Income and Poverty Rate')
    plt.xlabel('Median Annual Income ($)')
    plt.ylabel('Poverty Rate (%)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(title='State')
    
    plt.tight_layout()
    plt.savefig('visualizations/income_vs_poverty.png')
    plt.close()
    
    
    # Create a visualization comparing different unit sizes and their affordability
    plt.figure(figsize=(14, 8))
    
    # Calculate rent burden for each unit size
    df['burden_0br'] = (df['rent_50_0'] / df['monthly_income']) * 100
    df['burden_1br'] = (df['rent_50_1'] / df['monthly_income']) * 100
    df['burden_2br'] = (df['rent_50_2'] / df['monthly_income']) * 100
    df['burden_3br'] = (df['rent_50_3'] / df['monthly_income']) * 100
    df['burden_4br'] = (df['rent_50_4'] / df['monthly_income']) * 100
    
    # Group by state and calculate mean values
    burden_by_state = df.groupby('state').agg({
        'burden_0br': 'mean',
        'burden_1br': 'mean',
        'burden_2br': 'mean',
        'burden_3br': 'mean',
        'burden_4br': 'mean'
    }).reset_index()
    
    # Reshape data for easier plotting
    burden_long = pd.melt(
        burden_by_state, 
        id_vars=['state'], 
        value_vars=['burden_0br', 'burden_1br', 'burden_2br', 'burden_3br', 'burden_4br'],
        var_name='unit_size', 
        value_name='rent_burden'
    )
    
    # Map unit size to more readable labels
    unit_size_map = {
        'burden_0br': 'Studio',
        'burden_1br': '1-Bedroom',
        'burden_2br': '2-Bedroom',
        'burden_3br': '3-Bedroom',
        'burden_4br': '4-Bedroom'
    }
    burden_long['unit_size'] = burden_long['unit_size'].map(unit_size_map)
    
    # Create grouped bar chart
    sns.barplot(x='state', y='rent_burden', hue='unit_size', data=burden_long)
    
    plt.title('Rent Burden by Unit Size and State')
    plt.xlabel('State')
    plt.ylabel('Rent Burden (% of Monthly Income)')
    plt.axhline(y=30, color='r', linestyle='--', label='30% Affordability Threshold')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Adjust legend and labels
    plt.legend(title='Unit Size')
    
    plt.tight_layout()
    plt.savefig('visualizations/rent_burden_by_unit_size.png')
    plt.close()
