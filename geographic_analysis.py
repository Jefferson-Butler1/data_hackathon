#!/usr/bin/env python3
"""
Geographic analysis module for Section 8 Housing Data Analysis
This module analyzes geographic distribution of housing data
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_geographic_distribution(df):
    """
    Analyze and visualize geographic distribution of housing metrics
    
    Args:
        df (pd.DataFrame): The preprocessed housing data
    """
    # Top 10 counties by median rent
    plt.figure(figsize=(12, 8))
    
    # Get top 10 counties by median rent
    top_rent_counties = df.sort_values('median_rentE', ascending=False).head(10)
    
    # Create bar chart
    sns.barplot(x='median_rentE', y='county_name', data=top_rent_counties, hue='state', dodge=False)
    
    plt.title('Top 10 Counties with Highest Median Rent')
    plt.xlabel('Median Monthly Rent ($)')
    plt.ylabel('County')
    
    # Add value labels
    for i, v in enumerate(top_rent_counties['median_rentE']):
        plt.text(v + 10, i, f'${int(v)}', va='center')
    
    plt.tight_layout()
    plt.savefig('visualizations/top_10_highest_rent_counties.png')
    plt.close()
    
    # Bottom 10 counties by median rent
    plt.figure(figsize=(12, 8))
    
    # Get bottom 10 counties by median rent
    bottom_rent_counties = df.sort_values('median_rentE').head(10)
    
    # Create bar chart
    sns.barplot(x='median_rentE', y='county_name', data=bottom_rent_counties, hue='state', dodge=False)
    
    plt.title('10 Counties with Lowest Median Rent')
    plt.xlabel('Median Monthly Rent ($)')
    plt.ylabel('County')
    
    # Add value labels
    for i, v in enumerate(bottom_rent_counties['median_rentE']):
        plt.text(v + 10, i, f'${int(v)}', va='center')
    
    plt.tight_layout()
    plt.savefig('visualizations/bottom_10_lowest_rent_counties.png')
    plt.close()
    
    # Create a visualization comparing urban vs rural areas
    plt.figure(figsize=(12, 8))
    
    # Identify urban counties (with population > 100,000)
    df['area_type'] = df['total_popE'].apply(lambda x: 'Urban' if x > 100000 else 'Rural')
    
    # Group by area type and calculate mean values
    area_stats = df.groupby('area_type').agg({
        'median_rentE': 'mean',
        'median_incomeE': 'mean',
        'poverty_rate': 'mean',
        'rent_burden': 'mean'
    }).reset_index()
    
    # Create a multi-bar chart
    metrics = ['median_rentE', 'poverty_rate', 'rent_burden']
    metric_labels = ['Median Rent ($)', 'Poverty Rate (%)', 'Rent Burden (%)']
    
    x = np.arange(len(metrics))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    urban_data = area_stats[area_stats['area_type'] == 'Urban']
    rural_data = area_stats[area_stats['area_type'] == 'Rural']
    
    urban_values = [urban_data['median_rentE'].values[0], 
                   urban_data['poverty_rate'].values[0],
                   urban_data['rent_burden'].values[0]]
    
    rural_values = [rural_data['median_rentE'].values[0], 
                   rural_data['poverty_rate'].values[0],
                   rural_data['rent_burden'].values[0]]
    
    # Scale down the median rent for better visualization
    urban_values[0] = urban_values[0] / 10
    rural_values[0] = rural_values[0] / 10
    
    rects1 = ax.bar(x - width/2, urban_values, width, label='Urban')
    rects2 = ax.bar(x + width/2, rural_values, width, label='Rural')
    
    ax.set_ylabel('Value')
    ax.set_title('Comparison of Housing Metrics: Urban vs Rural Areas')
    ax.set_xticks(x)
    ax.set_xticklabels(metric_labels)
    ax.legend()
    
    # Add value labels
    def autolabel(rects):
        for i, rect in enumerate(rects):
            height = rect.get_height()
            # For the first metric (median rent), multiply by 10 to show actual value
            label_value = height
            if i == 0:
                label_value = height * 10
                ax.annotate(f'${int(label_value)}',
                           xy=(rect.get_x() + rect.get_width() / 2, height),
                           xytext=(0, 3),  # 3 points vertical offset
                           textcoords="offset points",
                           ha='center', va='bottom')
            else:
                ax.annotate(f'{label_value:.1f}%',
                           xy=(rect.get_x() + rect.get_width() / 2, height),
                           xytext=(0, 3),  # 3 points vertical offset
                           textcoords="offset points",
                           ha='center', va='bottom')
    
    autolabel(rects1)
    autolabel(rects2)
    
    # Add a note about scaling
    plt.figtext(0.5, 0.01, 'Note: Median Rent values are divided by 10 for scale compatibility', 
                ha='center', fontsize=10, style='italic')
    
    plt.tight_layout()
    plt.savefig('visualizations/urban_vs_rural_comparison.png')
    plt.close()
