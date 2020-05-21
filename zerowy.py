# zadanie 1
# importowanie biblioteki pandas
import pandas as pd
df = pd.DataFrame(pd.read_csv("train.tsv", delimiter="\t",names =['Price', 'Rooms','Area','Floor','Address','Description'], encoding='utf-8'))
print(df)
# zeby poprawnie otworzyc plik tsv za pomoca biblioteki pandas nalezy uzyc delimiter
#zadanie 2
print("Jedna kolumna")
print(df[["Price"]])

print("dwie kolumny")
print(df[["Price", "Floor"]])

print("all")
pd.set_option('max_colwidth', None)
print(df.head())
# zadanie 3
print(df.info())
# mamy doczynienia ze zmiennymi  dyskretnymi oraz ciągłymi zmiennymi dyskretnymi jest Rooms oraz Floor
# zmiennymi ciągłymi są Price oraz metry mieszkania
# zmienne District oraz description są tekstem

# zestaw 1
# zad 1
import csv
df = pd.DataFrame(pd.read_csv("train.tsv",
                              delimiter="\t",
                              names =['Price', 'Rooms','Area','Floor','Address','Description'],
                              encoding='utf-8'))

with open ('out0.csv',"w") as csv_write:
    writer = csv.writer(csv_write)
    writer.writerow([df.Price.mean().round()])