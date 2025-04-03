import requests
from exchanges.exchange_api import ExchangeAPI

class KrakenAPI(ExchangeAPI):
  def __init__(self):
    self.url = "https://api.kraken.com/0"
  
  def get_price(self, symbol: str) -> float:
    response = requests.get(f"{self.url}/public/Ticker?pair={symbol}")
    try:
      response.raise_for_status()
      data = response.json()
      return float(data["result"]["XBTUSDT"]["a"][0])
    except requests.exceptions.HTTPError as e:
      raise RuntimeError(f"HTTP error al obtener precio de Kraken: {e}")