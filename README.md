# Section 8 Housing Data Analysis - 2025 Hackathon

## Project Overview
This project analyzes Section 8 housing data in the Pacific Northwest from 2023. The analysis focuses on rent distribution, affordability metrics, geographic patterns, and the relationship between income and housing costs.

## Dataset
The dataset contains information about Section 8 housing across different counties in the Pacific Northwest states, including:
- Location identifiers (state codes, county codes, etc.)
- Rent information (median rents for different bedroom sizes)
- Census Bureau data (median income, poverty population, total population)

## Project Structure
- `main.py`: Main script that orchestrates the entire analysis pipeline
- `setup.py`: Script to set up the project environment and copy data
- `data_loader.py`: Module for loading and preprocessing the dataset
- `rent_analysis.py`: Module for analyzing rent distribution and affordability
- `geographic_analysis.py`: Module for analyzing geographic distribution
- `income_analysis.py`: Module for analyzing income, poverty, and housing relationships
- `visualizations/`: Directory where all generated visualizations are stored

## Visualizations Generated
1. Rent distribution by bedroom size
2. Average rent by state
3. Relationship between median income and median rent
4. Rent burden distribution
5. Top 10 counties with highest median rent
6. 10 counties with lowest median rent
7. Urban vs. rural comparison of housing metrics
8. Relationship between median income and poverty rate
9. Correlation matrix of housing and economic indicators
10. Rent burden by unit size and state

## How to Run the Project
1. Ensure you have Python 3.6+ installed
2. Install required dependencies:
   ```
   pip install pandas numpy matplotlib seaborn
   ```
3. Run the setup script:
   ```
   python setup.py
   ```
4. Run the main analysis:
   ```
   python main.py
   ```
5. View the generated visualizations in the `visualizations/` directory

## Analysis Insights
The analysis provides insights into:
- Rent affordability across different unit sizes
- Geographic patterns of housing costs
- Relationship between income, poverty, and housing costs
- Urban vs. rural housing cost differences
- Correlation between different economic and housing indicators

## Requirements
- Python 3.6+
- pandas
- numpy
- matplotlib
- seaborn
