import requests
from lxml import html

def getStockSymbols():
    """
    This function uses the lxml webscraping library to gather the stock symbols for the stocks in the DJIA.

    Returns:
    stockSymbols (list): List of the ticker symbols of all the stocks in the DJIA.
    """

    url = "https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average"
    webpage = requests.get(url)
    tree = html.fromstring(webpage.content)
    table = tree.xpath('//table[@id="constituents"]')[0]
    stockSymbols = []

    for row in table.xpath(".//tr")[1:]:
        symbol = row.xpath('.//td[3]//text()')[0].strip()
        stockSymbols.append(symbol)

    return stockSymbols

def getUserStocks(stockSymbols):
    """
    This function takes the user's input on the stocks they own and the number of shares they own of each stock.

    Parameters:
    - stockSymbols(list): List of stockSymbols in the DJIA. Will be used in an error handling feature that verifies that every stock they entered is in the DJIA.
    
    Returns:
    - ownedStocks(dict): Dictionary of all owned stocks, keys are the stock's ticker symbol and the values are the number of shares of that stock owned.
    """
    try:
        stocksNoAmount = input("Please enter the symbols for the stocks you own, separated by a space (ex. AAPL MSFT IBM): ")
        stocksNoAmount = stocksNoAmount.split(" ")

        ownedStocks = {}

        for i in stocksNoAmount:
            while True:
                try:
                    num = int(input("Enter the number of shares of " + i + " you own: "))
                    if num < 0:
                        print("Number of shares must be a positive integer. Please try again.")
                    else:
                        ownedStocks[i] = num
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
        
        return ownedStocks
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return None
                



