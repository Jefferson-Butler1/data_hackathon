import pandas as pd
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


