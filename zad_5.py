import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# read dataset
df = pd.read_csv("survey_results_schema.csv", encoding= "UTF-8")
df_2 = pd.read_csv("survey_results_public.csv",encoding = "UTF-8",
                   usecols=["Respondent","YearsCodePro","WorkWeekHrs"],
                   index_col= "Respondent")

df_2 = pd.DataFrame(df_2)

print(df_2.shape)
# delete Nan value
df_2_delete_nan = df_2.dropna()

print(df_2_delete_nan)

print(df_2_delete_nan.shape)
print(df_2_delete_nan.dtypes)
print(df_2_delete_nan.info())
# check column value and print unique value
columns_values = df_2_delete_nan[["YearsCodePro"]].values
unique_values = np.unique(columns_values)
print(unique_values)
# replace non numeric value to numeric
df_2_delete_nan = df_2_delete_nan.replace(to_replace={"Less than 1 year":"0"})
# check col value
columns_values = df_2_delete_nan[["YearsCodePro"]].values
unique_values = np.unique(columns_values)
print(unique_values)
# value to int64
df_2_delete_nan = df_2_delete_nan.astype("int64", copy=False)
print(df_2_delete_nan.dtypes)
# prepare plot in matplitlib
plt.plot(df_2_delete_nan["YearsCodePro"], df_2_delete_nan["WorkWeekHrs"], "ro", markersize=0.3)
plt.xlabel("YearsCodePro")
plt.ylabel("WorkWeekHrs")
plt.show()