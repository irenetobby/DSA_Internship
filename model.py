import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
# 1. Load the data
df = pd.read_csv(r'C:\Internship\cleaned_output.csv', sep=';')
# Standardize text columns to handle case-sensitivity
for col in ['Language', 'Genre', 'Format']:
    df[col] = df[col].astype(str).str.strip().str.capitalize()
df.columns = df.columns.str.strip() # Remove any hidden spaces

# 2. PERFORM FEATURE ENGINEERING FIRST (Crucial Step)
# You must create the column before you can use it in 'features'
df['Price_Bucket'] = pd.cut(df['Price'], bins=[0, 400, 900, 10000], labels=['Budget', 'Mid', 'Premium'])
df['Review_Density'] = df['Reviews'] / df['Pages']

# 3. Define your Features using EXACT capitalization
# Note: 'Rating' and 'Reviews' must be capitalized as per your dataset
features = ['Language', 'Genre', 'Price', 'Pages', 'Rating', 'Reviews', 'Format', 'Price_Bucket']
categorical_cols = ['Language', 'Genre', 'Format', 'Price_Bucket']

# 4. Fit Encoders on the FULL dataset columns
encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    le.fit(df[col].astype(str)) 
    encoders[col] = le

# 5. Take your sample
df_sample = df.sample(n=50000, random_state=42)

# 6. Prepare X and y from the sample
X = df_sample[features].copy()
y = df_sample['Success_Category']

# 7. Transform the categorical columns

for col in categorical_cols:
    X[col] = encoders[col].transform(X[col].astype(str))