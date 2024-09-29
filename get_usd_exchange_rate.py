import requests


def get_usd_exchange_rate():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        usd_rate = data["Valute"]["USD"]["Value"]
        return usd_rate
    else:
        print("Не удалось получить данные.")
        return None
