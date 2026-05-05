import pandas as pd

df = pd.read_csv("train.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

missing_values = df.isnull().sum()
print(missing_values)

duplicates = df.duplicated().sum()
print(duplicates)

df = df.drop_duplicates()

df = df.ffill()
df = df.bfill()

for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].astype(str)

for col in df.columns:
    if 'date' in col.lower():
        try:
            df[col] = pd.to_datetime(df[col])
        except:
            pass

numeric_cols = df.select_dtypes(include=['int64','float64']).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

for col in numeric_cols:
    df[col] = df[col].apply(lambda x: x if x >= 0 else 0)

if len(numeric_cols) >= 2:
    col1 = numeric_cols[0]
    col2 = numeric_cols[1]
    df['new_feature'] = df[col1] + df[col2]

df = df.reset_index(drop=True)

print(df.head())
print(df.describe())

df.to_csv("C:/Users/mulla/OneDrive/Desktop/Apex internship/cleaned_data.csv", index=False)
print("FILE SAVED SUCCESSFULLY")