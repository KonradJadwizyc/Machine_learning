import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

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
student_map = {"Yes, full-time": 1, "Yes, part-time": 1, "No": 0}
data_public["Student"] = data_public["Student"].map(student_map)

# One-Hot Encoding
data_public = data_public[(data_public["Gender"] == "Man") | (data_public["Gender"] == "Woman")]
data_public = pd.get_dummies(data_public, columns=["Gender"])
print(data_public)

# show correlation between data
print(data_public.corr(method='pearson'))

# Removing outliers
Q1 = data_public.quantile(0.25)
Q3 = data_public.quantile(0.75)
IQR = Q3 - Q1
data_public = data_public[~((data_public < (Q1 - 1.5 * IQR)) | (data_public > (Q3 + 1.5 * IQR))).any(axis=1)]

# Y variable: "YearsCodePro"
# X1 and X2 variables: "Age" & "Age1stCode"

# Create linear regression models
reg1 = linear_model.LinearRegression()
reg1.fit(data_public[["Age"]], data_public["YearsCodePro"])
print("Coefficients: \n", reg1.coef_)
# calculating MSE
print("MSE: \n %.2f"
      % mean_squared_error(data_public["YearsCodePro"], reg1.predict(data_public[["Age"]])))

reg2 = linear_model.LinearRegression()
reg2.fit(data_public[["Age", "Age1stCode"]], data_public["YearsCodePro"])
print("Coefficients: \n", reg2.coef_)
print("MSE: \n %.2f"
      % mean_squared_error(data_public["YearsCodePro"], reg2.predict(data_public[["Age", "Age1stCode"]])))

reg3 = linear_model.LinearRegression()
reg3.fit(data_public[["Age", "Age1stCode", "Student", "Gender_Man", "Gender_Woman"]], data_public["YearsCodePro"])
print("Coefficients: \n", reg3.coef_)
print("MSE: \n %.2f"
      % mean_squared_error(data_public["YearsCodePro"],
                           reg3.predict(data_public[["Age", "Age1stCode", "Student", "Gender_Man", "Gender_Woman"]])))