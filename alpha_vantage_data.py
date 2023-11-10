from alpha_vantage.timeseries import TimeSeries

def getHistoricalData(ownedStocks, startDate, endDate):
    """
    Using the Alpha Vantage API key, this function fetches historical stock prices for the given set of stocks in the specified date range. It then multiplies them by the number of each stock owned, which prepares the dataset for the portfolio metric calculations.
    Parameters:
    - ownedStocks (dict): A dictionary with stock symbols as keys and the number of shares owned as values.
    - startDate (str): Start date in the format 'YYYY-MM-DD'.
    - endDate (str): End date in the format 'YYYY-MM-DD'.

    Returns:
    - stockData: A pandas dataframe containing the historical total value of each company's stock the user owns over the specified period.
    """
    
    alphaVantageApiKey = "3UJTQ4SMTK48OBZK"
    ts = TimeSeries(key=alphaVantageApiKey, output_format='pandas')

    stockData = {}

    for symbol, num_shares in ownedStocks.items():
        try:
            data, _ = ts.get_daily(symbol=symbol, outputsize='full')
            data = data[(data.index >= startDate) & (data.index <= endDate)]
            
            #Sorts the data in ascending order by date
            data = data.sort_index(ascending=True)

            stockData[symbol] = data['4. close'] * num_shares
        except Exception as e:
            print(f"An error occurred while fetching data for {symbol}: {str(e)}")

    return stockData