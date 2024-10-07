from datetime import date
from typing import List

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)
    
    def remove_stock(self, stock):
        self.stocks.remove(stock)
    
    def value_on_date(self, date):
        """
        Calculate the total value of the portfolio on a given date.

        :param date: The date for which to calculate the portfolio value.
        :return: The total value of the portfolio on the given date.
        """
        return sum(stock.price(date) for stock in self.stocks)
    
    def profit(self, start_date, end_date):
        """
        Calculate the cumulative return of the portfolio between two dates.

        :param start_date: The start date for calculating the return.
        :param end_date: The end date for calculating the return.
        :return: The cumulative return of the portfolio as a float. This is calculated as the difference
                 between the portfolio's value at the end date and its value at the start date, divided
                 by the portfolio's value at the start date.
        """
        initial_value = self.value_on_date(start_date)
        final_value = self.value_on_date(end_date)
        return (final_value - initial_value) / initial_value
    
    def annualized_return(self, start_date, end_date):
        """
        Calculate the annualized return of the portfolio between two dates.

        :param start_date: The start date for calculating the annualized return.
        :param end_date: The end date for calculating the annualized return.
        :return: The annualized return of the portfolio as a float. This is calculated by taking the
                 cumulative return of the portfolio between the start and end dates and annualizing it
                 based on the number of days between those dates. The annualized return represents the
                 hypothetical yearly return rate if the portfolio's performance during the period were
                 to be extended over a full year.
        """
        total_return = self.profit(start_date, end_date)
        days = (end_date - start_date).days
        annualized_return = (1 + total_return) ** (365 / days) - 1
        return annualized_return
