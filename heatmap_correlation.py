import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv("marketing_data_featured.csv")


# Select numeric columns
final_data = pd.concat((df["Total_Children"], df["Age"], df["Total_Spending"]) , axis=1)
# Compute correlation matrix
corr_matrix = final_data.corr()

# Apply threshold: keep only strong correlations
'''threshold = 0.5
filtered_corr = corr_matrix.copy()
filtered_corr[np.abs(filtered_corr) < threshold] = 0  # Set weak correlations to 0'''

# Plot heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5, linecolor='black', data=corr_matrix, cbar_kws={"shrink": .8})
plt.title(f" Correlation Heatmap ")
plt.tight_layout()
plt.show()
