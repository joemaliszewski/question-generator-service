import pandas as pd

# Replace 'filename.csv' with your file path
df = pd.read_csv('/Users/vinegar/code/question-generator-service/data/chicken_broad-match_us_2023-10-03.csv')

# To see the first few rows of the dataframe
print(df.head())
