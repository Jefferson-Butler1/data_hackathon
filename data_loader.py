#!/usr/bin/env python3
"""
Data loader module for Section 8 Housing Data Analysis
This module handles loading and initial preprocessing of the dataset
"""
import pandas as pd

def load_data(file_path):
    """
    Load and preprocess the Section 8 housing dataset
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Cleaned and preprocessed dataframe
    """
    # Load the data
    df = pd.read_csv(file_path)
    
    # Clean up column names (remove trailing whitespace)
    df.columns = df.columns.str.strip()
    
    # Extract state information
    df['state'] = df['state_alpha']
    
    # Create poverty rate column
    df['poverty_rate'] = (df['poverty_popE'] / df['total_popE']) * 100
    
    # Calculate average rent across all bedroom sizes
    df['avg_rent'] = df[['rent_50_0', 'rent_50_1', 'rent_50_2', 'rent_50_3', 'rent_50_4']].mean(axis=1)
    
    # Calculate monthly income based on annual median income
    df['monthly_income'] = df['median_incomeE'] / 12
    
    # Create rent burden column (avg_rent / monthly_income)
    df['rent_burden'] = (df['avg_rent'] / df['monthly_income']) * 100
    
    # Clean up the HUD area name (remove quotes)
    df['hud_areaname'] = df['hud_areaname'].str.replace('"', '')
    
    return df
