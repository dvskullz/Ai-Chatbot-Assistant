import requests

def convert_currency(amount, from_currency, to_currency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
        data = requests.get(url).json()
        rate = data["rates"][to_currency.upper()]
        converted = float(amount) * rate
        return f"{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}"
    except Exception:
        return "Sorry, I couldn't convert the currency."