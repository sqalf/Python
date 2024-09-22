# Lê o .csv e imprime todas as pessoas com mais de 30 anos

import csv

with open('teste2.csv', newline='') as arquivo:
    reader = csv.DictReader(arquivo)
    
    for line in reader:
        idade = int(line['idade'])

        if idade > 30:
            print(line)
