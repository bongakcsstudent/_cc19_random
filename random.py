# Importing Data from the local device. 
from google.colab import files
uploaded = files.upload()


# Importing necessary libraries and reading uploaded data
import pandas as pd
import io
df = pd.read_csv(io.BytesIO(uploaded['anxiety_attack_dataset.csv']))
print(df)
# Identifying and printing missing data
missing_values = df.isnull()
print(missing_values)
# Checks and prints missing data status
missing_values_count = df.isnull().sum().sum()
if missing_values_count == 0:
    print("No missing values in the data set, 'Anxiety Attack Data Set'.")
else:
    print(f"There are {missing_values_count}.")
# Checks duplicated values
df.duplicated()
#Uses the imported library for describing the data
descriptive_stats = df.describe()
print(descriptive_stats)
#Counts the number of rows and columns
num_rows = df.shape[0]
num_cols = df.shape[1]
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")
#Counts the number of rows and columns
categorical_cols = df.select_dtypes(include=['object']).columns
numerical_cols = df.select_dtypes(include=['number']).columns


num_categorical = len(categorical_cols)
num_numerical = len(numerical_cols)


print(f"Number of categorical columns: {num_categorical}")
print(f"Number of numerical columns: {num_numerical}")
