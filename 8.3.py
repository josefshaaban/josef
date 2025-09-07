import mysql.connector
from geopy.distance import distance

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="salasana",
    database="lentoasemat"
)
cursor = conn.cursor()

icao1 = input("Anna ensimmäisen lentoaseman ICAO-koodi: ").upper()
icao2 = input("Anna toisen lentoaseman ICAO-koodi: ").upper()

query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"

cursor.execute(query, (icao1,))
tulos1 = cursor.fetchone()

cursor.execute(query, (icao2,))
tulos2 = cursor.fetchone()

if tulos1 and tulos2:
    lat1, lon1 = tulos1
    lat2, lon2 = tulos2
    etaisyys = distance((lat1, lon1), (lat2, lon2)).km
    print(f"Lentokenttien {icao1} ja {icao2} välinen etäisyys: {etaisyys:.2f} km")
else:
    print("Toinen tai molemmat ICAO-koodit eivät löytyneet.")

cursor.close()
conn.close()
