import pandas as pd
import seaborn as sns
from sklearn.preprocessing import OrdinalEncoder    
# Load the dataset
df = pd.read_csv("marketing_data_final.csv")
# Ensure the 'Education' column is treated as categorical
df['Education'] = df['Education'].astype('category')
# Define the order for ordinal features
education_order = ['High School', 'Bachelor', 'Master', 'PhD']
# Apply ordinal encoding
ordinal_encoder = OrdinalEncoder(categories=[education_order])
df['Education_Encoded'] = ordinal_encoder.fit_transform(df[['Education']])
print("Encoded Education values:", df['Education_Encoded'].unique())
# Apply one-hot encoding to nominal features
df_encoded = pd.get_dummies(df, columns=['Marital_Status'], drop_first=False)
# Combine ordinal and one-hot encoded features
df_final = pd.concat([df.drop(['Education', 'Marital_Status', 'Country'], axis=1), 
                      df[['Education_Encoded']], 
                      df_encoded.drop(['Education', 'Country'], axis=1)], axis=1) 
df_final = df_final.loc[:, ~df_final.columns.duplicated()]

print("*******\n",df_final[['ID', 'Marital_Status_Single', 'Marital_Status_Married', 'Marital_Status_Divorced']].head(10))
 
# Save the final DataFrame
df_final.to_csv("marketing_data_encoded.csv", index=False)
print("Final DataFrame saved to 'marketing_data_encoded.csv'.")



