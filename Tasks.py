from crewai import Task
from textwrap import dedent
import datetime
from dateutil.relativedelta import relativedelta

current_date=datetime.date.today()
prev_date=current_date-relativedelta(months=1)

class StockMarketHelperTasks:

    def StockFinderTask(self, agent, location, stock_type, amount):
        return Task(
            description=dedent(f'''
            
            **Task**:Find the most suitable stock depending upon user preference.
            
            **Tool**:Use the Internet Search Tool Provided.
            
            **Tool Input**: The user Parameters given below
            
            **Expected Output**: *Get the Ticker Symbol of the Stock.
                                 *Information about stocks.See description given below to get idea about what type of
                                  information is to be gathered.
            
            **Description**:
                           
                            *Try to gather the answer of these questions in your information:
                            
                                  *How does the company makes money?
                                  *Are its products or services in demand?
                                  *How as the company performed in the past?
                                  *Are talented,experienced managers in charge?
                                  *Is the company positioned for growth and profitability?
                                  *How much debt does the company have?
                                  *What are the future projects of the company
                                  
                            
            **Parameters:You can use the following parameters to find the most suitable stock for the user to invest in:
              [Location]: {location}
              [Type of Stock]: {stock_type}
              [Amount User can spend]: {amount}
              [Date]: {datetime.date.today().strftime("%d/%m/%Y")}
              
              '''),

            agent=agent


        )
    def StockReviewerTask(self,agent,context):
        return Task(
            description=dedent(f"""
            **Task**: Gather the reviews about the stock of the company which was selected by the task provided in the 
                      context.
                      
            **Tool**: Use Stock Reviewer Tool 
            
            **Tool Input**: Ticker symbol of the selected stock obtained from Stock Finder Task.
            
            **Expected Output**: Reviews about the stock found by the Stock Finder task.
            
            **Description**:
                             *Try to include at least 2-3 reviews
"""),
            context=context,
            agent=agent

        )

    def StockAnalystTask(self, agent, location, context: list):
        return Task(
            description=dedent(f'''
            **Task** : Gather news which can affect the stock prices of the stock you have selected from Stock Finder Task.
            
            **Tool**: News Finder Tool
            
            **Tool Input**: Name of the stock selected by the Stock Finder Task and the Parameters provided below.
            
            **Expected Output**: Gathering News about that stock and how it is affecting it.See the description to get
                                 idea about what type of news to be gathered.
            
            **Description** : 
                                *Given below are some news articles that may affect a stock.So you have to collect such 
                                 news and also provide a detailed explanation about how these news will affect the stock
                                 you have collected:
                                 
                              
                                   *Economic factors including interest rate changes, financial outlook and inflation
                                   *Government decisions on taxation, regulations, and fiscal policies
                                   *Politics
                                   *Interest Rate and Inflation
                                   *Natural Disasters
                                   *Economic Numbers
                                   *Gold Prices and Bonds
                                   *Trends in the industries
                                   *Market Sentiments
                                   *Monetary Policy of RBI and Regulatory Policies of SEBI
                                   *Foreign Institutional Investors (FIIs) and Domestic Institutional Investors (DIIs)
                                
                                *Try to gather at least 3-5 news articles and the description about how they might affect
                                the stock.
                              
                              
                              
            **Parameters** : You can use the following parameters to gather the news articles:
                             [LOCATION]: {location}
                             [TIME RANGE]: From-{prev_date} To-{current_date}
            '''),

            agent=agent,
            context=context

        )

    def StockPredictorTask(self, agent, context: list):
        return Task(
            description=dedent(f'''
                        **TASK**: Predict the profit or loss the stock selected by Stock Finder Task will make.
                        
                        **INPUT**: Historical Data collected by the Stock History task.
                        
                        **Expected Output**: Profit/Loss the user would make with proper explanation.Have a look on
                                             description to get idea about how to predict the profit or loss of stock.
                        
                        **Description**: 
                        
                                         *Predict whether the user makes loss or profit and how much loss or profit the 
                                         user can made at timestamp of every 1 month upto the next 6 months
                                         
                                         *If the stock price at timestamp in future is greater than the price of the stock
                                         at current timestamp then it is a profit otherwise it is a loss.
                                         
                                         *Calculate the profit/loss by subtracting the value of stock price in future and
                                         stock price at current timestamp.
                                         
                                    
                                         *Use the following features to predict the loss/profit the user van make:
                                                * Data of observation
                                                * Opening price
                                                * Highest price during trading day
                                                * Lowest price during trading day
                                                * Close price
                                                * News affecting the stocks
                                                
                                        *You have to predict the Closing price of the stock by using the above features.
                                        
                                        
                                         
                        **PARAMETERS**:
                        [Current Date]: {datetime.date.today().strftime("%d/%m/%Y")}
                        '''),
            agent=agent,
            context=context


        )

    def BestTimeToSellStockTask(self,agent,context):
        return Task(
            description=dedent(f"""
            
            **Task**: Your task is to decide which will be the best time for selling the stock.
            
            **INPUT**: Predictions made by the Stock Predictor task about the selected stock.
            
            **Expected Output**: Best time to sell the stock with proper explanation.
            
            **Description**: Use the information of the stock predictor task and decide which is the best time to sell the
                            stock such that the user can expect maximum possible profit.                  
                              
                              """)
        )
    def StockResearcherTask(self,agent,context:list):
        return Task(
            description=dedent(f'''
                      **Task**: Collect historical data about the selected stock from Stock Finder Task.
                      
                      
                      **Tool**: Use the Stock History tool.
                      **Tool input**: Just provide the ticker symbol of the selected stock and nothing else.
                      
                      **Expected Output**: Historical data about the stocks.See the description to get the idea about what
                                           type of data is to be collected.
                      
                      **Description**:
                                      
                                      *The historical data consist of the following points:
                                      
                                            *Opening price of the stock
                                            *Highest price during trading day
                                            *Lowest price during trading day
                                            *Closing price of the stock
                                            *Adjusted closing price of the stock
                                            *Volume of the stock
                                            
                                      *Provide the above information for every month upto 6 months before
                                      
                                      *You also have to provide the information about how these values differ from the 
                                       current values of stock.
                                       
                                       
                      **Parameters**:
                        [Current Date]: {datetime.date.today().strftime("%d/%m/%Y")}
                        [Ticker Symbol]: "Use the ticker symbol gathered during stock finder task"
                    '''

            ),

            agent=agent,
            context=context


        )

    def ReportProviderTask(self,agent,context):
        return Task(
            description=dedent(f"""
            
            **Task**: You have to use all the information gathered by the tasks provided in the context and generate a
                      detail report about it.
            
                      
                             """),

            expected_output=dedent(f"""
            ---------------------------------------------------------------------------------------------                      
                             
                             --------STOCK-INFO--------
                
                **COMPANY NAME**:
                
                **TICKER SYMBOL OF THE COMPANY**:
                
                **OPENING PRICE OF THE STOCK** :
                
                **CLOSING PRICE OF THE STOCK**:
                
                **LOWEST PRICE OF THE STOCK DURING DAY**:
                
                **HIGHEST PRICE OF THE STOCK DURING DAY**:
                
                **VOLUME OF THE STOCK**:
                
                **PRODUCTS AND SERVICES OFFERED BY THE COMPANY** :
            
                **GROWTH OF THE COMPANY** :
                
                **PROFITS MADE BY THE COMPANY** :
                
                **COMPANY'S PAST PERFORMANCE** :
                
                **DEBTS ON THE COMPANY** :
                
                **CEO OF THE COMPANY** :
                
                **FUTURE PROJECTS OF THE COMPANY** :
                
                *RETURN OF INVESTMENT OFFERED BY THE COMPANY**:
                
                **REVIEWS ABOUT THE STOCKS OF THE COMPANY**:
                
                
                -----------------------------------------------------------------------------------
                                
                                -----Factors Affecting Stock------
                       
                *News Headline*:
                       
                 *How it affects Stock*:
                 
                 
                ------------------------------------------------------------------------------------
                
                                 -------Stock Researcher-------
                               
                *DATE:
                               
                *Average Opening Price of Stock:
                               
                *Average Closing Price of Stock:
                               
                *Average Highest Price of Stock:
                               
                *Average Lowest Price of Stock:
                               
                *Average Adjusted Closing Price:
                               
                *Average Volume of Stock:
                               
                *Explanation how these values differ from current stock values:
                
                ----------------------------------------------------------------------------------------
                
                            ---------Stock Predictor-------
                          
                * Date:
                    
                * Buying Price of Stock (In Indian Ruppees):
                    
                * Expected Profit/Loss:
                    
                * Description:   
                
                --------------------------------------------------------------------------------------------
                
                *Best Time to sell Stock:
                
                *Reasons:
                
                --------------------------------------------------------------------------------------------            
                                  
                                  """),
            agent=agent,
            context=context
        )
