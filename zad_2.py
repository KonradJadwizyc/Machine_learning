# zad 2
import csv
import pandas as pd
df = pd.DataFrame(pd.read_csv("train.tsv",
                              delimiter="\t",
                              names =['Price', 'Rooms','Area','Floor','Address','Description'],
                              encoding='utf-8'))
df["Price_of_square_meter"] = df["Price"] / df["Area"]

with open ('out1.csv',"w") as csv_write:
    writer = csv.writer(csv_write, lineterminator = "\n")
    for i, row in df.iterrows():
        if row["Rooms"] >= 3 and (row["Price_of_square_meter"] < df.Price_of_square_meter.mean().round()):
            writer.writerow([row["Rooms"], row["Price"], row["Price_of_square_meter"]])