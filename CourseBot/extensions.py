import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CryptoConvertor:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException('Указанные одинаковые валюты ')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не правильный формат валюты "{quote}"')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не правильный формат валюты "{base}"')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Необходимо ввести число "{amount}"')

        r = requests.get(
            f'https://v6.exchangerate-api.com/v6/782e813e21ab1370e7e185ef/pair/{quote_ticker}/{base_ticker}/{amount}')
        total = json.loads(r.content)["conversion_result"], json.loads(r.content)["conversion_rate"]

        return total
