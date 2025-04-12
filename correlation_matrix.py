import matplotlib.pyplot as plt
import seaborn as sns

# Correlation matrix analysis module for Section 8 Housing Data Analysis
def correlation_matrix(df):

    # Create heatmap of correlation matrix
    plt.figure(figsize=(12, 10))
    
    # Select relevant columns for correlation
    corr_columns = [
        'median_incomeE', 'poverty_rate', 'total_popE', 
        'median_rentE', 'rent_50_0', 'rent_50_1', 'rent_50_2', 
        'rent_50_3', 'rent_50_4', 'rent_burden'
    ]
    
    # Rename columns for better readability in the heatmap
    corr_df = df[corr_columns].copy()
    corr_df.columns = [
        'Median Income', 'Poverty Rate', 'Population',
        'Median Rent', 'Studio Rent', '1BR Rent', '2BR Rent',
        '3BR Rent', '4BR Rent', 'Rent Burden'
    ]
    
    # Calculate correlation matrix
    corr_matrix = corr_df.corr()
    
    # Create heatmap
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Matrix of Housing and Economic Indicators')
    
    plt.tight_layout()
    plt.savefig('visualizations/correlation_heatmap.png')
    plt.close()
