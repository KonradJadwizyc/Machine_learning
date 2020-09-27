# import library
import pandas as pd


# read data
data_public = pd.read_csv("survey_results_public.csv",
                        usecols=["Respondent", "Age", "WorkWeekHrs", "YearsCodePro", "Age1stCode",
                                 "Gender", "Student", "CompTotal"],
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
# change data type to Str
data_public["Gender"] = data_public["Gender"].astype("str")

# print data type
print(data_public.dtypes)

# Converting text to numeric data
student_map = {"Yes, full-time": 1, "Yes, part-time": 2, "No": 0}
data_public["Student"] = data_public["Student"].map(student_map)

# One-Hot Encoding
data_public = data_public[(data_public["Gender"] == "Man") | (data_public["Gender"] == "Woman")]
data_public = pd.get_dummies(data_public, columns=["Gender"])
print(data_public)