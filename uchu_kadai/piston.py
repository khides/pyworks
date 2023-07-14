import pandas as pd
import openpyxl

df = pd.read_csv('piston.csv')
print(df.head())

df.to_excel('piston.xlsx')