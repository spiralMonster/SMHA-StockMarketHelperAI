from crewai import Agent
from textwrap import dedent
from langchain_google_genai import ChatGoogleGenerativeAI
from Tools.SearchTool import search_tool
from Tools.StockReviewer import stock_reviewer
from Tools.StockHistory import stock_history
from Tools.StockInformer import stock_informer
from Tools.NewsFinder import news_finder
from Tools.NameToTicker import name_to_ticker_symbol
from Tools.CalculateStock_Profit_Loss import calculate
class StockMarketHelperAgents:
    def __init__(self):
        self.llm=ChatGoogleGenerativeAI(model="gemini-pro")
    def StockFinder(self):
        return Agent(
            role="Stock Finder",
            goal="Give a detailed information about the stocks to invest in depending upon the current scenario and "
                 "user preferences.",
            backstory="You are a professional brocker in a stock market and you help the user to find the stocks to "
                      "invest in.",
            allow_delegation=True,
            verbose=False,
            tools=[search_tool.search_internet,
                   name_to_ticker_symbol.get_symbol,
                   stock_informer.get_information,],
            max_iter=5,
            llm=self.llm

        )

    def StockAnalyst(self):
        return Agent(
            role="Stock Analyzer",
            goal="You have to gather the news and provide description y about how these news might affect the stocks",
            backstory="You are an experienced stock analyzer who predicts the behaviour of stock depending upon the "
                      "ongoing events",
            allow_delegation=True,
            verbose=False,
            tools=[news_finder.find_news],
            max_iter=5,
            llm=self.llm
        )

    def StockResearcher(self):
        return Agent(
            role='Stock Researcher',
            goal="You have to provide the brief overview about the trends in the stock prices",
            backstory="You are an experienced Stock Researcher who has tons of information about the fluctuations in "
                      "stocks prices.",
            allow_delegation=True,
            verbose=False,
            tools=[stock_history.get_history],
            max_iter=5,
            llm=self.llm
        )

    def StockPredictor(self):
        return Agent(
            role="Stock Predictor",
            goal="You have to give a detail explanation about when to sell a stock and how much profit or loss the "
                 "user can expect and also predict the various values about stock after every one month.",
            backstory="You are an experienced Data Scientist who will predict the profit or loss made by selling the "
                      "stock in a given time period.",
            allow_delegation=True,
            verbose=False,
            tools=[calculate],
            max_iter=5,
            llm=self.llm
        )
    def ReportProviderAgent(self):
        return Agent(
            role="Report Creator",
            goal="""You have to provide a detailed report about all the information gathered through the tasks in the 
                  bulletin form.""",
            backstory="You are a experienced report writer who works for stock agencies.",
            allow_delegation=True,
            verbose=False,
            max_iter=5,
            llm=self.llm
        )
    def BestTimeToSellStockAgent(self):
        return Agent(
            role="Stock Brocker",
            goal="""Your job is to use the data about the predictions of stock price in the future and decide what will 
                    be the best time to sell the stock.""",
            backstory="You are an experienced stock brocker who has a good knowledge about the behaviour of stock market",
            allow_delegation=True,
            verbose=False,
            max_iter=5,
            llm=self.llm

        )
    def StockReviewerAgent(self):
        return Agent(
            role="Stock Reviewer",
            goal="You have to provide reviews about the stock of a company whether they are positive or negative",
            backstory="You are an experienced news reporter who is good at showcasing the public opinions.",
            allow_delegations=True,
            verbose=False,
            tools=[stock_reviewer.get_review],
            max_iter=5,
            llm=self.llm
        )


