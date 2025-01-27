//Upload Files 
//This is per task kaya iba-iba ung mga pinagiimport ko ha

//Task 1

from google.colab import files
uploaded = files.upload()

import pandas as pd
import io
df = pd.read_csv(io.BytesIO(uploaded['anxiety_attack_dataset.csv']))
print(df)

missing_values = df.isnull()
print(missing_values)


missing_values_count = df.isnull().sum().sum()
if missing_values_count == 0:
    print("No missing values in the data set, 'Anxiety Attack Data Set'.")
else:
    print(f"There are {missing_values_count}.")


df.duplicated()


descriptive_stats = df.describe()
print(descriptive_stats)

num_rows = df.shape[0]
num_cols = df.shape[1]
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")

categorical_cols = df.select_dtypes(include=['object']).columns
numerical_cols = df.select_dtypes(include=['number']).columns

num_categorical = len(categorical_cols)
num_numerical = len(numerical_cols)
print(f"Number of categorical columns: {num_categorical}")
print(f"Number of numerical columns: {num_numerical}")



// Ito na ung copy paste na part ;) ai overlords and cc8
// Removing extreeemee values w/ Quartiles 

import panda as pd

def rem_outlier(df, column_name);:
	Q1 = df[column_name].quantile(0.25)
	Q3 = df[column_name].quantile(0.75)
	IQR = Q3-Q1
	lower_bound = Q1 - 1.25*IQR
	upper_bound = Q3 + 1.25*IQR 
	df_filtered = df[(df[column_name] >= lower_bound) & (df[column_name] <= upper_bound)]
	return df_unfiltered

for col in numerical_cols:
	df = remove_outliers(df, col)

df

// Transforming Categorical Data to Numerical Data 
	
from sklearn.preprocessing 
import LabelEncoder 
import MinMaxScaler

label_encoder = LabelEncoder() 
for col in categorical_cols 
	df[col] = label_encoder.fit_transform(df[col])

df
 
// holds data frame w/ outliers removed/ updated lng

numerical_df = df[numerical_cols]
scaler = MinMaxScaler() 
normalized_data = scaler.fit_transform(numerical_df) 
normal_df = pd.DataFrame(normalized_data, columns=numerical_cols)
final_df = pd.concat([normalized_df, df[categorical_cols]], axis=1) 
final_df

