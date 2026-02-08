import pandas as pd

df = pd.read_csv("datasets/clients.csv")

print(df)

# ajouter une colonne
df["age_plus_5"] = df["age"] + 5
print(df)
