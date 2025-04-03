# 🧠 Crypto Exchanges Strategy Pattern

Este proyecto es un ejemplo sencillo que muestra cómo implementar el **patrón de diseño Strategy** en Python para interactuar con distintas APIs de exchanges de criptomonedas (como Binance, Kraken...).

## 🧩 Strategy Pattern

**Patrón Strategy**, permite definir una familia de algoritmos, encapsular cada uno y hacerlos intercambiables sin cambiar el código que los usa.

### 💡 En este contexto:

| Rol en el patrón Strategy | En el proyecto                            |
|---------------------------|-------------------------------------------|
| **Estrategia (Strategy)** | `ExchangeAPI` (interfaz abstracta)        |
| **Estrategias concretas** | `BinanceAPI`, `KrakenAPI`...                 |

Cada exchange representa una estrategia distinta para obtener precios. Al implementar la misma interfaz (`ExchangeAPI`), pueden ser intercambiados en tiempo de ejecución sin modificar la lógica del `CryptoTrader`.

## 📁 Estructura del Proyecto

```text
exchanges_hub/
│
├── exchanges/
│   ├── binance.py         # Implementación de BinanceAPI
│   ├── kraken.py          # Implementación de KrakenAPI
│   ├── exchange_api.py    # Interfaz base (ExchangeAPI)
│
├── crypto_trader.py       # Clase que implementa el patrón Strategy
├── main.py                # Script principal para ejecutar la demo
