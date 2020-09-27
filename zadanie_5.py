import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plot

# read data
data_public = pd.read_csv("survey_results_public.csv",
                        usecols=["Respondent", "Age", "YearsCodePro", "Age1stCode"],
                        index_col="Respondent")

# drop null
data_public.dropna(inplace=True)
# Converting text to numeric data
data_public = data_public.replace(to_replace={"Younger than 5 years":"0"})
data_public = data_public.replace(to_replace={"Older than 85":"90"})
data_public = data_public.replace(to_replace={"Less than 1 year":"0"})
data_public = data_public.replace(to_replace={"More than 50 years":"55"})

# change data type to float
data_public["Age1stCode"] = data_public["Age1stCode"].astype("float64")
data_public["YearsCodePro"] = data_public["YearsCodePro"].astype("float64")

# print data type
print(data_public.dtypes)

# show correlation between data
print(data_public.corr(method='pearson'))

plot.scatter(data_public["Age"], data_public["YearsCodePro"])
plot.title("Age depending on Years code pro")
plot.xlabel("Age")
plot.ylabel("Years Code Pro")
plot.show()

plot.scatter(data_public["Age1stCode"], data_public["YearsCodePro"])
plot.title("Years of coding depending on Age of starting programming")
plot.xlabel("Age of starting programming")
plot.ylabel("Years of coding")
plot.show()

# Removing outliers
Q1 = data_public.quantile(0.25)
Q3 = data_public.quantile(0.75)
IQR = Q3 - Q1
data_public = data_public[~((data_public < (Q1 - 1.5 * IQR)) | (data_public > (Q3 + 1.5 * IQR))).any(axis=1)]

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