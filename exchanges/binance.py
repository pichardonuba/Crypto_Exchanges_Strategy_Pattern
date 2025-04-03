import requests
from exchanges.exchange_api import ExchangeAPI

class BinanceAPI(ExchangeAPI):
  def __init__(self):
    self.url = "https://api.binance.com/api/v3"
    
  def get_price(self, symbol: str) -> float:
    response = requests.get(f"{self.url}/ticker/price?symbol={symbol}")
    try:
      response.raise_for_status()
      data = response.json()
      return float(data["price"])
    except requests.exceptions.HTTPError as e:
      raise RuntimeError(f"HTTP error al obtener precio de Binance: {e}")

    print(f"Orden {order_type} de {amount} en {symbol} en Binance")

    """Autentica con Binance usando las credenciales proporcionadas."""
    # Aquí, podrías usar la API oficial de Binance para hacer la autenticación
    self.api_key = api_key
    self.api_secret = api_secret
    
    # Simulación de autenticación exitosa (en un caso real, verificarías la clave con la API de Binance)
    if self.api_key == "my_valid_api_key" and self.api_secret == "my_valid_api_secret":
      print("Autenticación exitosa con Binance.")
      return True
    else:
      print("Error de autenticación con Binance.")
      return False