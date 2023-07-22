import requests
import json

class Connector:
    def get_btc(self):
        url = f'https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=2'
        response_json = json.loads(requests.get(url).text)
        return [float(response_json[0][4]), float(response_json[1][4])]
    def get_eth(self):
        url = f'https://fapi.binance.com/fapi/v1/klines?symbol=ETHUSDT&interval=1m&limit=2'
        response_json = json.loads(requests.get(url).text)
        return [float(response_json[0][4]), float(response_json[1][4])]

connector = Connector()