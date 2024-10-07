from datetime import date
from urllib import request
class Stock:
    def __init__(self, id: str):
        """
        :param id: Identifier of the stock.
        """
        self.id = id
    
    def price(self, date: date) -> float:
        """
        Retrieve the price of the stock on a given date.

        :param date: The date for which to retrieve the price.
        :return: The price of the stock on the given date.
        """