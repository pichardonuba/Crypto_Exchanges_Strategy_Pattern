from exchanges.binance import BinanceAPI
from exchanges.kraken import KrakenAPI
from crypto_trader import CryptoTrader

if __name__ == "__main__":
  binance = BinanceAPI()
  kraken = KrakenAPI()

  symbol = "BTCUSDT"
  crypto_trader = CryptoTrader(binance)  # Inyectamos Binance por defecto
  price_binance = crypto_trader.get_price(symbol)
  print(f"precio de {symbol} con binance {price_binance}")

  print("\nCambiando a Kraken...")
  crypto_trader.set_exchange(kraken)
  price_kraken = crypto_trader.get_price(symbol)
  print(f"precio de {symbol} con kraken {price_kraken}")