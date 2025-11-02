from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# --- 1. Alkuluvun tarkistus ---
def onko_alkuluku(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:luku>', methods=['GET'])
def alkuluku(luku):
    tulos = {
        "Number": luku,
        "isPrime": onko_alkuluku(luku)
    }
    return jsonify(tulos)


# --- 2. Lentokenttätiedon haku ---
# Oletetaan, että käytössä on sama tietokanta kuin kurssilla: "lentokentat.db"
# ja taulu on nimeltään 'airport' (tai 'airports'), jossa sarakkeet:
# ident (ICAO), name, municipality.

@app.route('/kenttä/<string:icao>', methods=['GET'])
def hae_kentta(icao):
    yhteys = sqlite3.connect('lentokentat.db')
    yhteys.row_factory = sqlite3.Row
    kursori = yhteys.cursor()

    kursori.execute("SELECT ident, name, municipality FROM airport WHERE ident = ?", (icao.upper(),))
    rivi = kursori.fetchone()
    yhteys.close()

    if rivi:
        tulos = {
            "ICAO": rivi["ident"],
            "Name": rivi["name"],
            "Municipality": rivi["municipality"]
        }
    else:
        tulos = {"error": "Lentokenttää ei löytynyt annetulla ICAO-koodilla."}

    return jsonify(tulos)


if __name__ == '__main__':
    app.run(port=3000, debug=True)
