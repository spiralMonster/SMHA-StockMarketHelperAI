from crewai import Agent
from textwrap import dedent

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
            tools=[]

        )

    def StockAnalyst(self):
        return Agent(
            role="Stock Analyst",
            goal="You have to analyse the ongoing events and give your insights about how these might affect the stocks",
            backstory="You are an experienced stock analyzer who predicts the behaviour of stock depending upon the "
                      "ongoing events",
            allow_delegation=True,
            verbose=True,
            tools=[]
        )

    def StockResearcher(self):
        return Agent(
            role='Stock Researcher',
            goal="You have to provide the brief overview about the trends in the stock prices",
            backstory="You are an experienced Stock Researcher who has tons of information about the fluctuations in "
                      "stocks prices.",
            allow_delegation=True,
            verbose=True,
            tools=[]
        )

    def StockPredictor(self):
        return Agent(
            role="Stock Predictor",
            goal="You have to give a detail explanation about when to sell a stock and how much profit or loss the "
                 "user can expect.",
            backstory="You are an experienced Data Scientist who will predict the profit or loss made by selling the "
                      "stock in a given time period.",
            allow_delegation=True,
            verbose=True,
            tools=[]
        )


