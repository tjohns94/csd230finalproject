import pandas as pd

def merge_csv(base_name):
    # Load the two halves from separate CSV files
    first_half = pd.read_csv(f'{base_name}-1.csv', encoding='cp949')
    second_half = pd.read_csv(f'{base_name}-2.csv', encoding='cp949')
    
    # Concatenate the two halves into a single DataFrame
    data = pd.concat([first_half, second_half])
    
    # Save the DataFrame into a single CSV file
    data.to_csv(f'{base_name}.csv', index=False, encoding='cp949')

# Example usage
for year in range(2013, 2023):
    base_name = f'C:/Users/sleep/OneDrive/CDS 230/Practice/data/국민건강보험공단_건강검진정보_{year}'
    merge_csv(base_name)