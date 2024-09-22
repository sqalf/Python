# Lê o .csv e imprime todas as pessoas com mais de 30 anos

import pandas as pd

df = pd.read_csv('csv.csv')

age30 = df[df['idade'] > 30]

print(age30)