import pandas as pd
import glob
from datetime import datetime

print("=== SALES PIPELINE START ===")

# Extract (plusieurs fichiers)

files = glob.glob("../datasets/sales_*.csv")

   # Mettre tout les dataFrame dans un seul tableau

df_list = []

for file in files:
    df = pd.read_csv(file)
    df_list.append(df)

sales = pd.concat(df_list)
print("sales :")
print(sales)

# Transform

  # Nettoyer

sales["quantity"] = sales["quantity"].fillna(0)
sales["price"] = sales["price"].fillna(0)

  # Nouvelle colonne revenue

sales["revenue"] = sales["quantity"] * sales["price"]

# KPI Business
  
  # KPI1 chiffre d'affaire total

ca_total = sales["revenue"].sum()
print("chiffre d'affaire total est :")
print(ca_total)


kpi_total_df = pd.DataFrame({
    "kpi": ["CA_total"],
    "value": [ca_total]
})

  # KPI2 chiffre d'affaire par ville

kpi_ville_df = (sales.groupby("city")["revenue"].sum().reset_index())
print("chiffre d'affaire par ville est :")
print(kpi_ville_df)


# ======================
# EXPORT CSV
# ======================

sales.to_csv("../datasets/sales_clean.csv", index=False)

today = datetime.today().strftime("%Y%m%d")

kpi_total_df.to_csv(f"../datasets/kpi_total_{today}.csv", index=False)
kpi_ville_df.to_csv(f"../datasets/kpi_par_ville_{today}.csv", index=False)

print("=== EXPORT DONE ===")