import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

# --- Step 1: Connect to MySQL ---
db_config = {
    'user': 'root',          # your MySQL username
    'password':'Sahithi@2003',  # your MySQL password
    'host': 'localhost',
    'database': 'customer_profitability_db'
}

# Using sqlalchemy for easy DataFrame to SQL transfer
engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")

# --- Step 2: Load Data from MySQL ---
query = "SELECT * FROM customer_profitability"
df = pd.read_sql(query, engine)

print("✅ Original Data Loaded:", df.shape)

# --- Step 3: Data Cleaning ---

# 1. Remove duplicate rows
df.drop_duplicates(inplace=True)

# 2. Handle missing values
df.fillna({
    'Gender': 'Unknown',
    'City': 'Unknown',
    'Segment': 'General',
    'Plan_Type': 'N/A'
}, inplace=True)

# 3. Remove invalid ages or profits
df = df[(df['Age'] > 0) & (df['Age'] < 100)]
df = df[df['Profit'] >= 0]

# 4. Standardize text columns (trim spaces, capitalize)
df['City'] = df['City'].str.strip().str.title()
df['Customer_Name'] = df['Customer_Name'].str.strip().str.title()

# 5. Recalculate Profit if inconsistent
df['Profit'] = df['Revenue'] - df['Cost']

# 6. Optional: Remove outliers (e.g., unusually high revenue)
upper_limit = df['Revenue'].quantile(0.99)
df = df[df['Revenue'] <= upper_limit]

print("✅ Cleaned Data:", df.shape)

# --- Step 4: Save Cleaned Data Back to MySQL ---
df.to_sql('customer_profitability_cleaned', con=engine, if_exists='replace', index=False)

print("✅ Cleaned data uploaded to 'customer_profitability_cleaned' table successfully!")
