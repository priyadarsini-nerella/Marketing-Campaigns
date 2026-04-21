import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, chi2_contingency, pearsonr, f_oneway

# Load and clean data
df = pd.read_csv("marketing_data.csv")

# Clean Income column
df['Income'] = df[' Income '].replace('[\$,]', '', regex=True).astype(float)

# Convert Dt_Customer to datetime
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], errors='coerce')

# Create new features
df['Age'] = 2025 - df['Year_Birth']
df['Tenure'] = 2025 - df['Dt_Customer'].dt.year
df['Children'] = df['Kidhome'] + df['Teenhome']
df['Total_Spend'] = df[['MntWines','MntFruits','MntMeatProducts','MntFishProducts','MntSweetProducts','MntGoldProds']].sum(axis=1)

# Drop rows with missing critical values
df.dropna(subset=['Income', 'Dt_Customer'], inplace=True)

# -------------------------------
# 📊 Exploratory Data Analysis
# -------------------------------

# Age distribution
sns.histplot(df['Age'], bins=30, kde=True)
plt.title("Age Distribution")
plt.show()

# Income distribution
sns.boxplot(x=df['Income'])
plt.title("Income Distribution")
plt.show()

# Spending by product category
spend_cols = ['MntWines','MntFruits','MntMeatProducts','MntFishProducts','MntSweetProducts','MntGoldProds']
df[spend_cols].mean().plot(kind='bar')
plt.title("Average Spend per Product Category")
plt.ylabel("Amount Spent")
plt.show()

# Response rate by marital status
response_rate = df.groupby('Marital_Status')['Response'].mean()
response_rate.plot(kind='bar')
plt.title("Response Rate by Marital Status")
plt.ylabel("Response Rate")
plt.show()

# -------------------------------
# 🧪 Hypothesis Testing
# -------------------------------

# H1: Income vs. Response
responders = df[df['Response'] == 1]['Income']
non_responders = df[df['Response'] == 0]['Income']
t_stat, p_val = ttest_ind(responders, non_responders, nan_policy='omit')
print(f"H1 - Income vs Response: t-stat={t_stat:.2f}, p-value={p_val:.4f}")

# H2: Marital Status vs. Response
contingency = pd.crosstab(df['Marital_Status'], df['Response'])
chi2, p, _, _ = chi2_contingency(contingency)
print(f"H2 - Marital Status vs Response: chi2={chi2:.2f}, p-value={p:.4f}")

# H3: Tenure vs. Response (Correlation)
corr, p_val = pearsonr(df['Tenure'].dropna(), df['Response'].dropna())
print(f"H3 - Tenure vs Response: correlation={corr:.2f}, p-value={p_val:.4f}")

# H4: Children vs. Response
contingency = pd.crosstab(df['Children'] > 0, df['Response'])
chi2, p, _, _ = chi2_contingency(contingency)
print(f"H4 - Children vs Response: chi2={chi2:.2f}, p-value={p:.4f}")

# H5: Education vs. Total Spend
groups = [group['Total_Spend'].dropna() for name, group in df.groupby('Education')]
f_stat, p_val = f_oneway(*groups)
print(f"H5 - Education vs Total Spend: F-stat={f_stat:.2f}, p-value={p_val:.4f}")
