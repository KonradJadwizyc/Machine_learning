import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# read dataset
df = pd.read_csv("survey_results_schema.csv", encoding= "UTF-8")
df_2 = pd.read_csv("survey_results_public.csv",encoding = "UTF-8",
                   usecols=["Respondent","Gender","WorkWeekHrs","Age","OrgSize"],
                   index_col= "Respondent")

df_2 = pd.DataFrame(df_2)

print(df_2.shape)
# delete Nan value
df_2 = df_2.dropna()

print(df_2)

print(df_2.shape)
print(df_2.dtypes)
print(df_2.info())

df_2["WorkWeekHrs"] = df_2["WorkWeekHrs"] / 40
column_values = df_2[["OrgSize"]].values
unique_values = np.unique(column_values)
print(unique_values)
# replace value
df_2 = df_2.replace(to_replace={"1,000 to 4,999 employees":"1,000 - 4,999"})
df_2 = df_2.replace(to_replace={"10 to 19 employees":"10 - 19"})
df_2 = df_2.replace(to_replace={"10,000 or more employees":"10,000 - more"})
df_2 = df_2.replace(to_replace={"2 to 9 employees":"2 - 9"})
df_2 = df_2.replace(to_replace={"100 to 499 employees":"100 - 499"})
df_2 = df_2.replace(to_replace={"20 to 99 employees":"20 - 99"})
df_2 = df_2.replace(to_replace={"5,000 to 9,999 employees":"5,000 - 9,999"})
df_2 = df_2.replace(to_replace={"500 to 999 employees":"500 - 999"})

column_values = df_2[["OrgSize"]].values
unique_values = np.unique(column_values)
print(unique_values)
# check col value
# value to int64
print(df_2.dtypes)
# prepare plot in matplitlib
# first plot
#gdf_2 = df_2.groupby("Gender")["WorkWeekHrs"].plot.barh()

plt.plot(df_2["WorkWeekHrs"],df_2["OrgSize"],"ro" ,markersize=0.5)
plt.xlabel("Work dayli")
plt.ylabel("Organization Size")
plt.show()

# second plot
val = [df_2.loc[df_2["Gender"] == "Man", "Age"],
        df_2.loc[df_2["Gender"] == "Woman", "Age"]]
fig = plt.figure(1,figsize=(9,6))
ax = fig.add_subplot(111)
bp = ax.boxplot(val, labels = list("MK"))
plt.title("Decomposition Age by Gender")
plt.ylabel("Age")
plt.show()