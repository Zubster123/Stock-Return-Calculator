from scraper_wiki_DJIA import getStockSymbols, getUserStocks
from alpha_vantage_data import getHistoricalData
from portfolio_metrics import calculatePortfolioMetrics

if __name__ == "__main__":
    djiaStockSymbols = getStockSymbols()
    ownedStocks = getUserStocks(djiaStockSymbols)

    #Specified start and end date in YYYY-MM-DD format
    startDate = "2020-01-01"
    endDate = "2023-01-01"

    stocksData = getHistoricalData(ownedStocks, startDate, endDate)
    meanDaily, stdDaily, cumulative = calculatePortfolioMetrics(stocksData, ownedStocks)

    print("\nPortfolio Metrics:")
    print("Mean Daily Return: ")
    print(str(meanDaily*100)+"%")
    print("\nStandard Deviation Of Daily Returns: ")
    print(str(stdDaily*100)+"%")
    print("\nCumulative Return: ")
    print(str(cumulative*100)+"%")
