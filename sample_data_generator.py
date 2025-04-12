#!/usr/bin/env python3
"""
Sample data generator for Section 8 Housing Data Analysis
This script creates a sample dataset based on the provided code book
"""
import pandas as pd
import numpy as np
import os

def generate_sample_data():
    """
    Generate a sample dataset based on the code book description
    
    Returns:
        pd.DataFrame: Generated sample data frame
    """
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Define states in the Pacific Northwest
    states = ['WA', 'OR', 'ID']
    state_codes = {'WA': 53, 'OR': 41, 'ID': 16}
    
    # Create empty dataframe
    rows = []
    
    # Generate data for each state
    for state in states:
        # Generate between 20-50 counties per state
        num_counties = np.random.randint(20, 50)
        
        for county_idx in range(1, num_counties + 1):
            # Generate basic county info
            county_name = f"{state} County {county_idx}"
            state_code = state_codes[state]
            county_code = county_idx
            county_sub_code = 99999
            
            # Determine if it's a metro area (1 in 3 chance)
            is_metro = np.random.random() < 0.3
            hud_areaname = f"{county_name}, {state} {'HUD Metro FMR Area' if is_metro else ''}"
            fips2010 = int(f"{state_code}{county_code:03d}{county_sub_code}")
            
            # Generate rent data based on whether it's metro or not
            base_rent = np.random.randint(600, 1500)
            if is_metro:
                base_rent += np.random.randint(200, 500)
                
            rent_50_0 = base_rent
            rent_50_1 = int(base_rent * (1 + np.random.uniform(0.1, 0.3)))
            rent_50_2 = int(rent_50_1 * (1 + np.random.uniform(0.2, 0.4)))
            rent_50_3 = int(rent_50_2 * (1 + np.random.uniform(0.3, 0.5)))
            rent_50_4 = int(rent_50_3 * (1 + np.random.uniform(0.1, 0.3)))
            
            # Generate HUD area code
            if is_metro:
                hud_area_code = f"METRO{np.random.randint(10000, 99999)}M{np.random.randint(10000, 99999)}"
            else:
                hud_area_code = f"NCNTY{state_code}{county_code:03d}N{state_code}{county_code:03d}"
            
            # Generate GEOID
            geoid = int(f"{state_code}{county_code:03d}")
            
            # Generate income and population data
            base_income = np.random.randint(40000, 100000)
            if is_metro:
                base_income += np.random.randint(5000, 20000)
                
            median_incomeE = base_income
            median_incomeM = int(base_income * np.random.uniform(0.01, 0.1))
            
            # Population
            base_pop = np.random.randint(5000, 500000)
            if is_metro:
                base_pop += np.random.randint(50000, 200000)
                
            total_popE = base_pop
            total_popM = int(base_pop * np.random.uniform(0.001, 0.05))
            
            # Poverty population - typically 5-25% of total population
            poverty_rate = np.random.uniform(0.05, 0.25)
            poverty_popE = int(total_popE * poverty_rate)
            poverty_popM = int(poverty_popE * np.random.uniform(0.05, 0.2))
            
            # Median rent (slightly different from HUD fair market rent)
            median_rentE = int(rent_50_1 * np.random.uniform(0.9, 1.1))
            median_rentM = int(median_rentE * np.random.uniform(0.01, 0.1))
            
            # Add row to data
            row = {
                'county_name': county_name,
                'state_alpha': state,
                'state_code': state_code,
                'county_code': county_code,
                'county_sub_code': county_sub_code,
                'hud_areaname': hud_areaname,
                'fips2010': fips2010,
                'rent_50_0': rent_50_0,
                'rent_50_1': rent_50_1,
                'rent_50_2': rent_50_2,
                'rent_50_3': rent_50_3,
                'rent_50_4': rent_50_4,
                'hud_area_code': hud_area_code,
                'GEOID': geoid,
                'median_incomeE': median_incomeE,
                'median_incomeM': median_incomeM,
                'poverty_popE': poverty_popE,
                'poverty_popM': poverty_popM,
                'total_popE': total_popE,
                'total_popM': total_popM,
                'median_rentE': median_rentE,
                'median_rentM': median_rentM
            }
            
            rows.append(row)
    
    # Create dataframe from rows
    df = pd.DataFrame(rows)
    
    return df

def save_sample_data(output_path='hackathonData2025.csv'):
    """
    Generate and save sample data to CSV
    
    Args:
        output_path (str): Path to save the CSV file
    """
    df = generate_sample_data()
    df.to_csv(output_path, index=False)
    print(f"Sample data saved to {output_path}")
    
    # Print data summary
    print("\nData Summary:")
    print(f"Number of rows: {len(df)}")
    print(f"Number of columns: {len(df.columns)}")
    print(f"States included: {', '.join(df['state_alpha'].unique())}")
    print(f"Rent ranges:")
    for col in ['rent_50_0', 'rent_50_1', 'rent_50_2', 'rent_50_3', 'rent_50_4']:
        print(f"  {col}: ${df[col].min()} to ${df[col].max()}")

if __name__ == "__main__":
    save_sample_data()
