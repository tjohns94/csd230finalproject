import pandas as pd

df = pd.read_csv('./data/국민건강보험공단_건강검진정보_2020.csv', encoding='cp949')
df.rename(columns={'체중(5Kg 단위)': '체중(5kg단위)'}, inplace=True)
df.to_csv('./data/국민건강보험공단_건강검진정보_2020.csv', index=False, encoding='cp949')