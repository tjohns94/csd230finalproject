import pandas as pd

# Define the range of years
years = range(2013, 2023)

# Create an empty dataframe
sk_nhic_records = pd.DataFrame()

# Read in the files for each year and append to the dataframe
for year in years:
    filename = f"./data/국민건강보험공단_건강검진정보_{year}.csv"
    data = pd.read_csv(filename, encoding='cp949', low_memory=False).dropna(how='all', axis=1)
    sk_nhic_records = sk_nhic_records._append(data)

# Create a sample of the data with 100,000 rows
sk_nhic_sample = sk_nhic_records.sample(n=10000)

# Save the sample to a new file
sk_nhic_sample.to_csv('./data/nhic_sample_small.csv', index=False, encoding='utf-8-sig')