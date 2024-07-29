from crewai import Agent
from textwrap import dedent
from Tools.SearchTool import search_tool
from Tools.StockReviewer import stock_reviewer
from Tools.StockHistory import stock_history
from Tools.StockInformer import stock_informer
from Tools.NewsFinder import news_finder
from Tools.NameToTicker import name_to_ticker_symbol
from Tools.CalculateStock_Profit_Loss import calculate
class StockMarketHelperAgents:
    def StockFinder(self):
        return Agent(
            role="Stock Finder",
            goal="Give a detailed information about the stocks to invest in depending upon the current scenario and "
                 "user preferences.",
            backstory="You are a professional brocker in a stock market and you help the user to find the stocks to "
                      "invest in.",
            allow_delegation=True,
            verbose=True,
            tools=[search_tool.search_internet,
                   name_to_ticker_symbol.get_symbol,
                   stock_informer.get_information,
                   stock_reviewer.get_review]

        )

    def StockAnalyst(self):
        return Agent(
            role="Stock Analyst",
            goal="You have to analyse the ongoing events and give your insights about how these might affect the stocks",
            backstory="You are an experienced stock analyzer who predicts the behaviour of stock depending upon the "
                      "ongoing events",
            allow_delegation=True,
            verbose=True,
            tools=[news_finder.find_news]
        )

    def StockResearcher(self):
        return Agent(
            role='Stock Researcher',
            goal="You have to provide the brief overview about the trends in the stock prices",
            backstory="You are an experienced Stock Researcher who has tons of information about the fluctuations in "
                      "stocks prices.",
            allow_delegation=True,
            verbose=True,
            tools=[stock_history.get_history]
        )

    def StockPredictor(self):
        return Agent(
            role="Stock Predictor",
            goal="You have to give a detail explanation about when to sell a stock and how much profit or loss the "
                 "user can expect and also predict the various values about stock after every one month.",
            backstory="You are an experienced Data Scientist who will predict the profit or loss made by selling the "
                      "stock in a given time period.",
            allow_delegation=True,
            verbose=True,
            tools=[stock_history.get_history,calculate]
        )


