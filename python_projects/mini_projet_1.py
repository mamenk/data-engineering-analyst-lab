# Lire clients.csv

import pandas as pd
import os

df = pd.read_csv("C:\\Users\\mamen\\Data_Engineering_Analyst_Lab\\datasets\\clients.csv")


# Ajouter une colonne “catégorie âge” 


def categorie_age(age):
    if age < 18:
        return "Mineur"
    elif age < 30:
        return "Jeune adulte"
    else:
        return "Adulte"

df["categorie"] = df["age"].apply(categorie_age)

# Filtrer les clients “Jeune adulte” et afficher

clients_jeunes_adultes = df[df["categorie"] == "Jeune adulte" ]
print("Clients jeunes adultes :")
print(clients_jeunes_adultes)

# Sauvegarder le résultat dans datasets/clients_output.csv

df.to_csv("C:\\Users\\mamen\\Data_Engineering_Analyst_Lab\\datasets\\clients_output.csv", index=False)