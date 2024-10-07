import unittest
from datetime import date
from portfolio import Portfolio
from stock import Stock

class StockMock(Stock):
    def __init__(self, id: str, price_data: dict):
        super().__init__(id)
        self.price_data = price_data
    
    def price(self, date: date) -> float:
        return self.price_data.get(date, 0.0)

class TestPortfolio(unittest.TestCase):
    def setUp(self):
        self.portfolio = Portfolio()
        stock1 = StockMock("AAPL", {
            date(2023, 1, 1): 150.0,
            date(2024, 1, 1): 180.0,
        })
        stock2 = StockMock("GOOGL", {
            date(2023, 1, 1): 100.0,
            date(2024, 1, 1): 120.0,
        })
        self.portfolio.add_stock(stock1)
        self.portfolio.add_stock(stock2)
    
    def test_profit(self):
        start_date = date(2023, 1, 1)
        end_date = date(2024, 1, 1)
        expected_profit = ((180.0 + 120.0) - (150.0 + 100.0)) / (150.0 + 100.0)
        self.assertAlmostEqual(self.portfolio.profit(start_date, end_date), expected_profit)
    
    def test_annualized_return(self):
        start_date = date(2023, 1, 1)
        end_date = date(2024, 1, 1)
        total_return = ((180.0 + 120.0) - (150.0 + 100.0)) / (150.0 + 100.0)
        expected_annualized_return = (1 + total_return) ** (365 / 365) - 1
        self.assertAlmostEqual(self.portfolio.annualized_return(start_date, end_date), expected_annualized_return)

if __name__ == '__main__':
    unittest.main()
