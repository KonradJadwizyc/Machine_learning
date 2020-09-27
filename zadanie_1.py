# import library
import pandas as pd
import matplotlib.pyplot as plot

# read data
data_public = pd.read_csv("survey_results_public.csv",
                        usecols=["Respondent", "Age", "WorkWeekHrs", "YearsCodePro", "Age1stCode", "CompTotal"],
                        index_col="Respondent")

# drop null
data_public.dropna(inplace=True)
# Converting text to numeric data
data_public = data_public.replace(to_replace={"Younger than 5 years":"0"})
data_public = data_public.replace(to_replace={"Older than 85":"90"})
data_public = data_public.replace(to_replace={"Less than 1 year":"0"})
data_public = data_public.replace(to_replace={"More than 50 years":"55"})
# Converting work week hrs
data_public["WorkWeekHrs"] = data_public["WorkWeekHrs"] / 40

# change data type to float
data_public["Age1stCode"] = data_public["Age1stCode"].astype("float64")
data_public["YearsCodePro"] = data_public["YearsCodePro"].astype("float64")
# print data type
print(data_public.dtypes)
# show correlation between data
print(data_public.corr(method='pearson'))

# Creating a plots

plot.scatter(data_public["Age"], data_public["YearsCodePro"])
plot.title("Age depending on Years code pro")
plot.xlabel("Age")
plot.ylabel("Years Code Pro")
plot.show()

plot.scatter(data_public["YearsCodePro"], data_public["CompTotal"])
plot.title("Years code pro depending on CompTotal")
plot.xlabel("Years Code Pro")
plot.ylabel("CompTotal")
plot.show()

plot.scatter(data_public["Age"], data_public["CompTotal"])
plot.title("Age depending on CompTotal")
plot.xlabel("Age")
plot.ylabel("CompTotal")
plot.show()

plot.scatter(data_public["Age1stCode"], data_public["Age"])
plot.title("Age 1st code depending on Age")
plot.xlabel("Age 1st Code")
plot.ylabel("Age")
plot.show()

plot.scatter(data_public["Age"], data_public["WorkWeekHrs"])
plot.title("Work Week Hrs depending on Age")
plot.xlabel("Age")
plot.ylabel("WorkWeekHrs")
plot.show()
# dependent variable: "YearsCodePro"
# independent variables: "Age" & "Age1stCode"