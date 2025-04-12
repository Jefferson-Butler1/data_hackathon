# this file compiles a list of averages for each column. Doesnt save it anywhere, but just prints it to stdout

import pandas as pd
import numpy as np

def calculate_averages(df):
    """
    Calculate the average for each ***NUMERICAL*** column in the DataFrame
    
    Args:
        df (pd.DataFrame): The DataFrame to calculate averages for
    """

    numericalColumns =     [ 	 "rent_50_0"	, "rent_50_1"	, "rent_50_2"	, "rent_50_3"	, "rent_50_4"	, "median_incomeE"	, "median_incomeM"	, "poverty_popE"	, "poverty_popM"	, "total_popE"	, "total_popM"	, "median_rentE"	, "median_rentM",]

    # averages the numerical columns and prints them, avoiding trying to calculat the average of non-numerical

    for column in numericalColumns:
        average = df[column].mean()
        print(f"{column}: {average:.2f}")
