# zad 3
import pandas as pd
import csv
df = pd.DataFrame(pd.read_csv("train.tsv",
                              delimiter="\t",
                              names =['Price', 'Rooms','Area','Floor','Address','Description'],
                              encoding='utf-8'))
df_2 = pd.DataFrame(pd.read_csv("description.csv",
                                delimiter= ",",encoding="utf-8"))

df_all = pd.merge(df,df_2, left_on="Rooms", right_on="liczba", how = "left")

with open ('out2.csv',"w") as csv_write:
   writer = csv.writer(csv_write)
   for i, row in df_all.iterrows():
    writer.writerow(row.values)