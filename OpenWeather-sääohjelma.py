import requests


def hae_saa():
    kaupunki = input("Anna paikkakunnan nimi: ")
    api_avain = "YOUR_API_KEY_HERE"  # <-- Syötä oma API-avaimesi tähän
    url = f"https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_avain}&lang=fi"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        kuvaus = data["weather"][0]["description"]  # esim. "selkeää"
        lampotila_kelvin = data["main"]["temp"]
        lampotila_celsius = lampotila_kelvin - 273.15  # Kelvin → Celsius

        print(f"Sää paikassa {kaupunki}: {kuvaus}")
        print(f"Lämpötila: {lampotila_celsius:.1f} °C")
    else:
        print("Säätietojen hakeminen epäonnistui. Tarkista paikkakunta tai API-avain.")


if __name__ == "__main__":
    hae_saa()
