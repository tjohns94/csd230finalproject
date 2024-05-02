import pandas as pd

columns_lists = []

health2022 = pd.read_csv('./data/국민건강보험공단_건강검진정보_2022.csv', encoding='cp949')
health2021 = pd.read_csv('./data/국민건강보험공단_건강검진정보_2021.csv', encoding='cp949')
health2020 = pd.read_csv('./data/국민건강보험공단_건강검진정보_2020.csv', encoding='cp949')
health2019 = pd.read_csv('./data/국민건강보험공단_건강검진정보_2019.csv', encoding='cp949')
health2018 = pd.read_csv('./data/국민건강보험공단_건강검진정보_2018.csv', encoding='cp949')
health2017 = pd.read_csv('./data/국민건강보험공단_건강검진정보_2017.csv', encoding='cp949')
health2016 = pd.read_csv('./data/국민건강보험공단_건강검진정보_2016.csv', encoding='cp949')
health2015 = pd.read_csv('./data/국민건강보험공단_건강검진정보_2015.csv', encoding='cp949')
health2014 = pd.read_csv('./data/국민건강보험공단_건강검진정보_2014.csv', encoding='cp949')
health2013 = pd.read_csv('./data/국민건강보험공단_건강검진정보_2013.csv', encoding='cp949')

health2022cols = []
for col in health2022.columns:
    health2022cols.append(col)

health2021cols = []
for col in health2021.columns:
    health2021cols.append(col)
    health2020cols = []
    for col in health2020.columns:
        health2020cols.append(col)

    health2019cols = []
    for col in health2019.columns:
        health2019cols.append(col)

    health2018cols = []
    for col in health2018.columns:
        health2018cols.append(col)

    health2017cols = []
    for col in health2017.columns:
        health2017cols.append(col)

    health2016cols = []
    for col in health2016.columns:
        health2016cols.append(col)

    health2015cols = []
    for col in health2015.columns:
        health2015cols.append(col)

    health2014cols = []
    for col in health2014.columns:
        health2014cols.append(col)

    health2013cols = []
    for col in health2013.columns:
        health2013cols.append(col)

columns_lists.append(health2022cols)
columns_lists.append(health2021cols)
columns_lists.append(health2020cols)
columns_lists.append(health2019cols)
columns_lists.append(health2018cols)
columns_lists.append(health2017cols)
columns_lists.append(health2016cols)
columns_lists.append(health2015cols)
columns_lists.append(health2014cols)
columns_lists.append(health2013cols)

col_counts = []
for cols in columns_lists:
    col_counts.append(len(cols))

col_intersection = set.intersection(*map(set, columns_lists))
print(len(col_intersection))
col_intersection = list(col_intersection)
years = ['2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013']
data = []

all_columns = set(col for sublist in columns_lists for col in sublist)
all_columns = list(all_columns)

for year, cols in zip(years, columns_lists):
    year_data = []
    for col in all_columns:
        if col in cols:
            year_data.append(True)
        else:
            year_data.append(False)
    data.append(year_data)

df = pd.DataFrame(data, columns=all_columns, index=years)
df.to_csv('./data/columns_info.csv', index=True, encoding='cp949')