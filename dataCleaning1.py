import pandas as pd

# Load the dataset
df = pd.read_csv("marketing_data_cleaned.csv")
# Check for complete duplicate rows
full_duplicates = df[df.duplicated(keep=False)]

# Check for duplicates based on a subset of columns (e.g., customer demographics)
subset_columns = ['Year_Birth', 'Education', 'Marital_Status', 'Income', 'Kidhome', 'Teenhome', 'Country','Response']
partial_duplicates = df[df.duplicated(subset=subset_columns, keep=False)]

# Display results
print("🔁 Full duplicate rows:")
print(full_duplicates)

print("\n🔁 Partial duplicates based on demographics:")
print(partial_duplicates)
df_no_partial_dupes = df.drop_duplicates(subset=subset_columns, keep='first')
print(f"✅ Dataset after dropping partial duplicates: {df_no_partial_dupes.shape[0]} rows.")



# Save the cleaned dataset  
df.to_csv("marketing_data_cleaned.csv", index=False)
print("\nCleaned data saved to 'marketing_data_cleaned.csv'.")