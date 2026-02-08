import pyodbc

conn = pyodbc.connect(
    "DRIVER={SQL Server};SERVER=localhost;DATABASE=master;Trusted_Connection=yes;"
)

print("Connexion OK")
