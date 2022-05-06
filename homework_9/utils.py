import requests


def lookup(currency):
    response = requests.get('https://bitpay.com/api/rates')

    data = response.json()
    result = ''

    for line in data:
        if line.get('code') == currency:
            result = line
    return result

