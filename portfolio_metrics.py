import pandas as pd

def calculatePortfolioMetrics(stockData, ownedStocks):
    """
    This function calculates the desired portfolio metrics.

    Parameters:
    - stockData (dataframe): A pandas dataframe containing the historical total value of each company's stock the user owns over the specified period.    
    - ownedStocks (dict): A dictionary with stock symbols as keys and the number of shares owned as values.

    Returns:
    - meanDailyReturnPercentage: Mean daily return as a percentage for the entire portfolio.
    - stdDevDailyReturn: Standard deviation of daily returns as a percentage for the entire portfolio.
    - cumulativeReturns: Cumulative return as a percentage for the entire portfolio at the end of the specified time period.
    """
    
    # Create a copy of the DataFrame to avoid modifying the original data
    portfolioDf = pd.DataFrame(stockData).copy()

    # Calculate the total value of the entire portfolio for each day
    totalPortfolioValue = portfolioDf.sum(axis=1)

    #Calculate the portfolio's daily percentage change over the specified time frame
    percentageChange = totalPortfolioValue.pct_change()

    # Calculate mean daily return
    meanDailyReturnPercentage = percentageChange.mean()

    # Calculate standard deviation of daily returns
    stdDevDailyReturn = percentageChange.std()

    # Calculate the portfolio's cumulative return at the end of the specified time period 
    cumulativeReturns = percentageChange.cumsum().iloc[-1]

    return meanDailyReturnPercentage, stdDevDailyReturn, cumulativeReturns