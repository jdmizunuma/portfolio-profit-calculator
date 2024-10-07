# Portfolio-Profit-Calculator

This repository implements a `Portfolio` class that allows for calculating the profit between two dates and the annualized return of a collection of stocks. It follows the instructions provided in the job application.

## Instructions

The task is to construct a simple `Portfolio` class that has a collection of stocks and a `Profit` method that receives 2 dates and returns the profit of the portfolio between those dates. Each stock has a `Price` method that receives a date and returns its price. The Bonus Track is to make the `Profit` method return the annualized return of the portfolio between the given dates.

## Project Structure

- **portfolio.py**: Contains the `Portfolio` class, which holds a collection of stocks and calculates the profit and annualized return.
- **stock.py**: Contains the `Stock` class, which represents individual stocks (used only for testing purposes).
- **test_portfolio.py**: Contains unit tests to verify the correctness of the portfolio’s profit and annualized return calculations.

## Portfolio Class

This class allows you to manage a collection of stocks and calculate the profit between two dates, as well as the annualized return.

## Formulas Used

### Cumulative Return

The cumulative return represents the percentage increase or decrease in the value of the portfolio over a given period. The formula used is:

Cumulative Return = (Final Value - Initial Value) / Initial Value

For more information, see [Investopedia - Cumulative Return](https://www.investopedia.com/terms/c/cumulativereturn.asp).

### Annualized Return

The annualized return calculates the hypothetical yearly return rate if the portfolio's performance during the given period were extended over a full year. The formula used is:

Annualized Return = (1 + Cumulative Return) ** (365 / Number of Days) - 1

For more information, see [Investopedia - Annualized Total Return](https://www.investopedia.com/terms/a/annualized-total-return.asp).

## Tests

To execute tests, run the following command in the command line:

`python -m unittest test_portfolio.py`
