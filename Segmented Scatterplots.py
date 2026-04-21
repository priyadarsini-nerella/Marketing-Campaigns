import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("marketing_data_featured.csv")

g = sns.FacetGrid(df, col="Education", col_wrap=3, height=4, aspect=1.2)
g.map_dataframe(sns.scatterplot, x="Age", y="Total_Spending", alpha=0.6, color="teal")
g.map_dataframe(sns.regplot, x="Age", y="Total_Spending", scatter=False, color="black", line_kws={"linewidth": 1.5})
g.set_axis_labels("Age", "Total Spending")
g.fig.suptitle("Spending Patterns by Education Level", fontsize=16)
g.fig.tight_layout()
g.fig.subplots_adjust(top=0.9)
plt.show()

g = sns.FacetGrid(df, col="Marital_Status", col_wrap=3, height=4, aspect=1.2)
g.map_dataframe(sns.scatterplot, x="Age", y="Total_Spending", alpha=0.6, color="coral")
g.map_dataframe(sns.regplot, x="Age", y="Total_Spending", scatter=False, color="black", line_kws={"linewidth": 1.5})
g.set_axis_labels("Age", "Total Spending")
g.fig.suptitle("Spending Patterns by Marital Status", fontsize=16)
g.fig.tight_layout()
g.fig.subplots_adjust(top=0.9)
plt.show()


# what to look for in the plots
# - The scatter plots show how Total Spending varies with Age across different education levels.
# - The trend lines indicate the general relationship; for example, higher education levels may correlate with higher spending.
# - Look for differences in spending patterns based on education, which can inform targeted marketing strategies.   