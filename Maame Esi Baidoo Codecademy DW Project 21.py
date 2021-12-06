import codecademylib3
import pandas as pd
import numpy as np

# code goes here
#Loading the data into a pandas dataframe
diabetes_data = pd.read_csv("diabetes.csv")
#Inspecting the data
print(diabetes_data.head())
print(diabetes_data.shape)
#Checking if there are any null values
print(diabetes_data.isnull().sum())
print(diabetes_data.info())
print(diabetes_data.describe())
#.describe() reveals there is 0 where there should not be zero indicating these are missing values
#Replacing every instance of 0 in these columns with NaN to make it easier to work with
diabetes_data[["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]] = diabetes_data[["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]].replace(0, np.nan)
#Checking if replacing with NaN was successful
print(diabetes_data.isnull().sum())
print(diabetes_data.head())
#Printing all the rows with missing values
print(diabetes_data[diabetes_data.isnull().any(axis = 1)])
#Checking the data type of each column
print(diabetes_data.dtypes)
#Checking the unique values in the outcome column which is an object instead of int to know why
print(diabetes_data.Outcome.unique())
#Contains o as well instead of 0
#Replacing all Os in the outcome column with 0 and converting the values to type int
diabetes_data.Outcome.replace("O", 0, inplace = True)
diabetes_data["Outcome"] = diabetes_data.Outcome.astype(int)
print(diabetes_data.Outcome.unique())
print(diabetes_data.dtypes)
#Counting the different values in the outcome column
print(diabetes_data["Outcome"].value_counts())