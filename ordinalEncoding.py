import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv("marketing_data_final.csv")
# Ensure the 'Education' column is treated as categorical
df['Education'] = df['Education'].astype('category')
# Define the order for ordinal features
education_order = ['High School', 'Bachelor','Master', 'PhD']

# Apply ordinal encoding
ordinal_encoder = OrdinalEncoder(categories=[education_order])
df['Education_Encoded'] = ordinal_encoder.fit_transform(df[['Education']])
df['Education_encoded'] = df['Education'].astype(
    pd.CategoricalDtype(categories=education_order, ordered=True)
).cat.codes
# Display the first few rows of the DataFrame to verify encoding
print("Encoded Education values:", df['Education_encoded'].head())
print("Encoded Education values:", df['Education_Encoded'].head())

# Apply one-hot encoding to nominal features
df_encoded = pd.get_dummies(df, columns=['Marital_Status'], drop_first=True)
# Display the first few rows of the DataFrame to verify encoding
print(df_encoded.head())

# Combine ordinal and one-hot encoded features
'''df_final = pd.concat([df.drop(['Education', 'Marital_Status', 'Country'], axis=1), 
                      df[['Education_Encoded']], 
                      df_encoded.drop(['Education', 'Marital_Status', 'Country'], axis=1)], axis=1)'''
# Save the final DataFrame
#df_final.to_csv("marketing_data_encoded.csv", index=False)