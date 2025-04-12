#!/usr/bin/env python3
"""
Main script for Section 8 Housing Data Analysis
This script coordinates the data loading and calls various analysis modules
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data
from rent_analysis import analyze_rent_distribution, rent_to_income_ratio
from geographic_analysis import analyze_geographic_distribution
from income_analysis import analyze_income_poverty_relation
from averages import calculate_averages
from correlation_matrix import correlation_matrix

def create_output_dir():
    """Create output directory for visualizations if it doesn't exist"""
    os.makedirs('visualizations', exist_ok=True)

def main():
    """Main function to orchestrate the data analysis pipeline"""
    # Create output directory
    create_output_dir()
    
    # Check if the data file exists, if not, generate sample data
    data_file = 'hackathonData2025.csv'

    # Load the data
    print("Loading data...")
    data = load_data(data_file)

    correlation_matrix(data)
    
#     # Run various analyses
#     print("Analyzing rent distribution...")
#     analyze_rent_distribution(data)
    
    print("Calculating rent to income ratios...")
    rent_to_income_ratio(data)
    # 
    # print("Analyzing geographic distribution...")
    # analyze_geographic_distribution(data)
    # 
    # print("Analyzing income and poverty relation...")
    # analyze_income_poverty_relation(data)
    
    print("Analysis complete. Visualizations saved in 'visualizations' directory.")

if __name__ == "__main__":
    main()
