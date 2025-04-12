#!/usr/bin/env python3
"""
Setup script for Section 8 Housing Data Analysis
This script copies the dataset and creates necessary directories
"""
import os
import shutil

def main():
    """Setup the project environment"""
    # Create visualizations directory if it doesn't exist
    os.makedirs('visualizations', exist_ok=True)
    
    # Copy the dataset file if it's not already in the project directory
    source_file = '../hackathonData2025.csv'
    dest_file = 'hackathonData2025.csv'
    
    if not os.path.exists(dest_file) and os.path.exists(source_file):
        shutil.copy(source_file, dest_file)
        print(f"Copied dataset from {source_file} to {dest_file}")
    elif not os.path.exists(dest_file):
        print(f"Warning: Could not find source dataset at {source_file}")
        print("Please manually place the hackathonData2025.csv file in the project directory.")
    else:
        print(f"Dataset already exists at {dest_file}")
    
    print("Setup complete!")

if __name__ == "__main__":
    main()
