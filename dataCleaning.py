import pandas as pd

# Load the dataset
df = pd.read_csv("marketing_data.csv")

# -------------------------------
# 🔍 1. Inspect 'Income' column
# -------------------------------

# Display first few values
print("Income sample values:")
print(df[' Income '].head())

# Remove currency symbols and convert to numeric
# Rename column for consistency
df.rename(columns={' Income ': 'Income'}, inplace=True)
df['Income'] = pd.to_numeric(
    df['Income'].astype(str).str.replace(r'[\$,]', '', regex=True),
    errors='coerce'
)

# Check for missing or invalid entries
print("\nIncome summary:")
print(df['Income'])
print("Missing Income values:", df['Income'].isnull().sum())

# -------------------------------
# 📅 2. Inspect 'Dt_Customer' column
# -------------------------------

# Display first few values
print("\nDt_Customer sample values:")
print(df['Dt_Customer'].head())

# Convert to datetime format
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d/%m/%y', errors='coerce')
df['Dt_Customer'] = df['Dt_Customer'].dt.strftime('%d/%m/%Y')

# Check for conversion issues
print("\nDt_Customer summary:")
print(df['Dt_Customer'])
print("Missing Dt_Customer values:", df['Dt_Customer'].isnull().sum())
df.dropna(subset=['Income', 'Dt_Customer'], inplace=True)
print("Missing values after cleaning:", df[['Income', 'Dt_Customer']].isnull().sum())
print(df['Income'].head())


# -------------------------------
# 📅 3. Inspect 'Education' , 'Marital_Status' column
# -------------------------------
df['Education'] = df['Education'].str.strip().str.title()
df['Marital_Status'] = df['Marital_Status'].str.strip().str.title()
print("df[Education]:", df['Education'].unique())
print("df[Marital_Status]:", df['Marital_Status'].unique())
valid_statuses = ['Single', 'Married', 'Divorced', 'Widow', 'Together']
df = df[df['Marital_Status'].isin(valid_statuses)]
df['Marital_Status'] = df['Marital_Status'].replace({'Together': 'Living Together'})
education_map = {
    'Basic': 'High School',
    'Graduation': 'Bachelor',
    'Master': 'Master',
    'Phd': 'PhD',
    '2N Cycle': 'Master'  # Assuming it's equivalent
}
df['Education'] = df['Education'].replace(education_map)
print("df[Education]:", df['Education'].unique())
print("df[Marital_Status]:", df['Marital_Status'].unique())


#load the cleaned data
df.to_csv("marketing_data_cleaned.csv", index=False)
print("\nCleaned data saved to 'marketing_data_cleaned.csv'.")
