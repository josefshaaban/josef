import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="salasana",
    database="lentoasemat"
)
cursor = conn.cursor()

maakoodi = input("Anna maakoodi (esim. FI): ").upper()

query = "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type"
cursor.execute(query, (maakoodi,))

tulokset = cursor.fetchall()
if tulokset:
    print(f"Lentokenttien lukumäärät maassa {maakoodi}:")
    for tyyppi, lkm in tulokset:
        print(f"{tyyppi}: {lkm} kpl")
else:
    print("Maakoodia ei löytynyt tai kenttiä ei ole.")

cursor.close()
conn.close()
