import mysql.connector

# Yhdistä tietokantaan
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="salasana",
    database="lentoasemat"
)
cursor = conn.cursor()

icao = input("Anna lentoaseman ICAO-koodi: ").upper()

query = "SELECT name, municipality FROM airport WHERE ident = %s"
cursor.execute(query, (icao,))

tulos = cursor.fetchone()
if tulos:
    nimi, kunta = tulos
    print(f"Lentokentän nimi: {nimi}")
    print(f"Sijaintikunta: {kunta}")
else:
    print("Lentokenttää ei löytynyt.")

cursor.close()
conn.close()
