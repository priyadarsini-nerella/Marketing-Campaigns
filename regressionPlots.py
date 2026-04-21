import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("marketing_data_featured.csv")

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Total_Spending', data=df, color='purple', alpha=0.6)

# Add a trend line
sns.regplot(x='Age', y='Total_Spending', data=df, scatter=False, color='black', line_kws={"linewidth": 2})

plt.title("Relationship Between Age and Total Spending")
plt.xlabel("Age")
plt.ylabel("Total Spending")
plt.grid(True)
plt.tight_layout()
plt.show()

# what to look for in the plot
# The plot shows the relationship between Age and Total Spending. 
# A positive trend indicates that as age increases, total spending tends to increase as well.
# This can suggest that older customers may have more disposable income or different spending habits.   