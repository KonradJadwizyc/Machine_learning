# zad 1
import pandas as pd
import csv
df = pd.DataFrame(pd.read_csv("train.tsv",
                              delimiter="\t",
                              names =['Price', 'Rooms','Area','Floor','Address','Description'],
                              encoding='utf-8'))

with open ('out1.csv',"w") as csv_write:
    writer = csv.writer(csv_write)
    writer.writerow([df.Price.mean().round()])