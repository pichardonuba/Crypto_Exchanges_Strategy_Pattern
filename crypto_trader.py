from exchanges.exchange_api import ExchangeAPI

class CryptoTrader:
  def __init__(self, exchange: ExchangeAPI):
    self.exchange = exchange  # Inyección de dependencias

  def set_exchange(self, exchange: ExchangeAPI):
    """Permite cambiar el exchange en tiempo de ejecución"""
    self.exchange = exchange

  def get_price(self, symbol: str) -> float:
    return self.exchange.get_price(symbol)
