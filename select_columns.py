########################################################
# Description: This script is used to create a new CSV #
# file with selected columns.                          #
########################################################

# Import libraries
import pandas as pd

# Load the CSV files into a DataFrame
# age_wwhs stands for age and waist circumference, weight, hearing, and sight
age_wwhs = pd.DataFrame()

# Load the CSV files for each year and concatenate them into one DataFrame
years = range(2013, 2023)
for year in years:
    file_path = f'./data/국민건강보험공단_건강검진정보_{year}.csv'
    temp_df = pd.read_csv(file_path, encoding='cp949', usecols=['기준년도', '연령대코드(5세단위)', '허리둘레', '체중(5kg단위)', '청력(좌)', '청력(우)', '시력(좌)', '시력(우)'])
    age_wwhs = pd.concat([age_wwhs, temp_df])

# Save the DataFrame into a single CSV file
age_wwhs.to_csv('./data/age_wwhs.csv', index=False, encoding='cp949')
