import pandas as pd
from datetime import datetime

# Load data
df = pd.read_csv("marketing_data_final.csv")

# 1️⃣ Total number of children
df['Total_Children'] = df['Kidhome'] + df['Teenhome']

# 2️⃣ Age (assuming current year is 2025)
current_year = datetime.now().year
df['Age'] = current_year - df['Year_Birth']

# 3️⃣ Total spending across product categories
spending_cols = [
    'MntWines', 'MntFruits', 'MntMeatProducts',
    'MntFishProducts', 'MntSweetProducts', 'MntGoldProds'
]
df['Total_Spending'] = df[spending_cols].sum(axis=1)

# 4️⃣ Total purchases across channels
purchase_cols = ['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']
df['Total_Purchases'] = df[purchase_cols].sum(axis=1)


import matplotlib.pyplot as plt
import seaborn as sns

target_cols = ['Total_Children', 'Age', 'Total_Spending', 'Total_Purchases']

'''for col in target_cols:
    plt.figure(figsize=(12, 5))

    # Histogram
    plt.subplot(1, 2, 1)
    sns.histplot(df[col], kde=True, bins=30, color='skyblue')
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)

    # Boxplot
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df[col], color='salmon')
    plt.title(f'Boxplot of {col}')
    plt.xlabel(col)

    plt.tight_layout()
    plt.show()'''
sns.set(style="whitegrid")
df_melted = df[target_cols].melt(var_name='Feature', value_name='Value')

g = sns.FacetGrid(df_melted, col="Feature", col_wrap=2, height=4, sharex=False, sharey=False)
g.map(sns.histplot, "Value", kde=True, bins=30, color='skyblue')
g.set_titles("{col_name}")
plt.tight_layout()
plt.show()
# what to look for in the plots
# - Histograms show the distribution of each feature, indicating skewness or normality.
# - Boxplots highlight outliers and the spread of the data.
# - The Age feature should show a typical age distribution, while Total Spending may show a right-skewed distribution due to high spenders.
# - Total Children and Total Purchases should also be examined for outliers and distribution patterns.  


# Save the feature-engineered dataset
df.to_csv("marketing_data_featured.csv", index=False)
print("✅ Feature-engineered dataset saved as 'marketing_data_featured.csv'.")