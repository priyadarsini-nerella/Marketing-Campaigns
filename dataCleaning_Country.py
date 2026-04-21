import pandas as pd

# Load the dataset
df = pd.read_csv("marketing_data_cleaned.csv")

# Step 1: Define columns to check for semantic duplicates (excluding ID and Country)
semantic_cols = df.columns.drop(['ID', 'Country'])
print("🔍 Identifying semantic duplicates based on columns:", semantic_cols.tolist())

# Step 2: Find semantic duplicates
semantic_dupes = df[df.duplicated(subset=semantic_cols, keep=False)].copy()
print("🔍 Identifying semantic duplicates..." ,semantic_dupes)
print(f"🔍 Found {len(semantic_dupes)} semantic duplicates (same data, different ID/Country).")

# Step 3: Flag them
semantic_dupes['Semantic_Duplicate_Flag'] = True

# Step 4: Resolve country (choose most frequent or first)
resolved_country = (
    semantic_dupes
    .groupby(list(semantic_cols))['Country']
    .agg(lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0])
    .reset_index()
)

# Step 5: Assign a canonical ID (e.g., lowest ID per group)
resolved_id = (
    semantic_dupes
    .groupby(list(semantic_cols))['ID']
    .min()
    .reset_index()
)

# Step 6: Merge resolved ID and Country back
resolved_profiles = pd.merge(resolved_id, resolved_country, on=list(semantic_cols))

# Step 7: Create cleaned dataset with deduplicated profiles
df_cleaned = pd.concat([
    df[~df.duplicated(subset=semantic_cols, keep=False)],
    resolved_profiles
], ignore_index=True)

# Save cleaned dataset
df_cleaned.to_csv("marketing_data_final.csv", index=False)
print("✅ Cleaned dataset saved as 'marketing_data_semantic_final.csv'.")
