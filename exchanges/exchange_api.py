from abc import ABC, abstractmethod

class ExchangeAPI(ABC):
  @abstractmethod
  def get_price(self, symbol: str) -> float:
    pass

