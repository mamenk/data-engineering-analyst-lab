import pandas as pd

print("=== START ETL ===")

# 1. Extract
df = pd.read_csv("../datasets/clients_raw.csv")

print("\nRaw data:")
print(df)

# 2. Transform (nettoyage)
df["age"] = df["age"].fillna(df["age"].mean())
df["city"] = df["city"].fillna("Unknown")
df["salary"] = df["salary"].fillna(0)

# KPI
avg_salary = df["salary"].mean()

print("\nCleaned data:")
print(df)

print(f"\nAverage salary: {avg_salary}")

# 3. Load (export propre)
df.to_csv("../datasets/clients_clean.csv", index=False)

print("\n=== ETL FINISHED ===")
