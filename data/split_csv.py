import pandas as pd

def split_csv(file_path):
    # Remove the .csv extension and prepare base names
    base_name = file_path[:-4]  # Assuming the file always ends with '.csv'
    
    # Load the CSV file into a DataFrame
    data = pd.read_csv(file_path, encoding='cp949')
    
    # Calculate the middle index
    middle_index = len(data) // 2
    
    # Split the DataFrame into two halves
    first_half = data.iloc[:middle_index]
    second_half = data.iloc[middle_index:]
    
    # Save the two halves into separate CSV files with '-1' and '-2' appended
    first_half.to_csv(f'{base_name}-1.csv', index=False, encoding='cp949')
    second_half.to_csv(f'{base_name}-2.csv', index=False, encoding='cp949')

# Example usage
for year in range(2013, 2023):
    file_path = f'C:/Users/sleep/OneDrive/CDS 230/Practice/data/국민건강보험공단_건강검진정보_{year}.csv'
    split_csv(file_path)