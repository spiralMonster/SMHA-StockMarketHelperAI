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
            
            **Task**:Find top stocks in which the agent can invest depending upon the current scenario.
            
            **Description**:
                           *You have to search top 5 stocks depending upon the current scenario and user preferences from 
                           the Internet.
                           
                           *Then get the ticker symbols for these stocks.
                           
                           
                           *Provide the information gathered about the stocks in a bulletin form.You should include this
                            information in the expected output format as provided.
                           
                            *It is expected from you to add answers to these questions in your explanation:
                            
                                  *How does the company makes money?
                                  *Are its products or services in demand?
                                  *How as the company performed in the past?
                                  *Are talented,experienced managers in charge?
                                  *Is the company positioned for growth and profitability?
                                  *How much debt does the company have?
                                  
                            *Gather all these information from internet using search tool and add it in appropriate location
                             in the expected output.
                                  
                            *Try to include the reviews about the stock use ticker symbol as input to get and include it under
                            appropriate location in expected output.
                            
                            **Compulsion: You have to provide at least top 5 stocks
                            
                            **Important Note:First complete all tasks of one stock then start the task of other one.
                                            Add output of the other stock just below the output of previous stock
                            
            **Parameters:You can use the following parameters to find the top 5 stocks for the user to invest in:
              [Location]: {location}
              [Type of Stock]: {stock_type}
              [Amount User can spend]: {amount}
              [Date]: {datetime.date.today().strftime("%d/%m/%Y")}
              
              '''),
            expected_output=dedent(
                f'''
                Given below is the template of how the expected outcome should be.
                You can add your own points which you feel are relevant in the case.
                
                ------STOCK-INFO--------
                
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
                '''),

            agent=agent,
            async_execution=True

        )

    def StockAnalystTask(self, agent, location, context: list):
        return Task(
            description=dedent(f'''
            **Task** : Gather news which can affect the stock prices you have gathered.
            **Description** : Collect news and provide a detailed explanation in the form of bulletin that how those news will affect the
                              stock prices.
                              
                              The news article you can gather could be:
                              
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
                              
                              Using these news article give a proper explanation about how these news will affect the stock price both in positive and negative way.
                              
                              *Compulsion: You have to provide at least 3 to 5 news for each stock gathered by the stock 
                              finder task.
                              
            **Parameters** : You can use the following parameters to gather the news articles:
                             [LOCATION]: {location}
                             [TIME RANGE]: From-{prev_date} To-{current_date}
            '''),

            expected_output=dedent(f'''
                       
                       
                       -----Factors Affecting Stock------
                       
                       *News Headline*:
                       
                       *How it affects Stock*:
                       
                    '''

                                   ),
            agent=agent,
            asyn_execution=True,
            context=context

        )

    def StockPredictorTask(self, agent, context: list):
        return Task(
            description=dedent(f'''
                        **TASK**: Predict the profit or loss the user would make by using the historical data of the stocks 
                                  you have collected.
                        
                        **Description**: Collect the historical data regarding the stocks and predict whether 
                                         the user makes loss or profit and how much loss or profit the user can
                                         made at different timestamps.
                                         
                                         *If the stock price at timestamp in future is greater than the price of the stock
                                         at current timestamp then it is a profit otherwise it is a loss.
                                         
                                         *Calculate the profit/loss by subtracting the value of stock price in future and
                                         stock price at current timestamp.
                                         
                                        *So you have to provide that information for every month upto 6 months.
                                         
                                         *You can predict the profit/loss using the following features:
                                                * Data of observation
                                                * Opening price
                                                * Highest price during trading day
                                                * Lowest price during trading day
                                                * Close price
                                                * News affecting the stocks
                                                
                                        Here Close price is the dependent feature.
                                        
                                        *After predicting the values for stocks for upto 6 months then in the end provide
                                        the time range in which the user can sell the stocks such that they can get maximum
                                        possible profit.
                        **PARAMETERS**:
                        [Current Date]: {datetime.date.today().strftime("%d/%m/%Y")}
                        '''),
            agent=agent,
            context=context,
            asyn_execution=True,
            expected_output=dedent(f'''
                          ------Stock Predictor------
                          
                    * Date:
                    
                    * Buying Price of Stock (In Indian Ruppees):
                    
                    * Expected Profit/Loss:
                    
                    * Description:
            '''
                                   )

        )
    def StockResearcherTask(self,agent,context:list):
        return Task(
            description=dedent(f'''
                      **Task**: Collect historical data about stocks using their ticker symbol.
                      **Description**: 
                                      *Using the ticker symbol of the stock get the historical data about those stocks.
                                      
                                      *The historical data consist of the following points:
                                      
                                            *Opening price of the stock
                                            *Highest price during trading day
                                            *Lowest price during trading day
                                            *Closing price of the stock
                                            *Volume of the stock
                                        
                                     *Compare these values of the stock with their current values and also provide a 
                                     detailed explanation about how these parameters change with the current values of stock.
                                     
                                     *Compulsion:You have to provide all the mentioned information for every month in the
                                      expected output format as provided.
            
            
                      **Parameters**:
                        [Current Date]: {datetime.date.today().strftime("%d/%m/%Y")}
                    '''

            ),
            expected_output=dedent(f"""
                            
                               ---------------Stock Researcher-----------------
                               
                               *DATE:
                               
                               *Average Opening Price of Stock:
                               
                               *Average Closing Price of Stock:
                               
                               *Average Highest Price of Stock:
                               
                               *Average Lowest Price of Stock:
                               
                               *Average Volume of Stock:
                               
                               *Explanation how these values differ from current stock values:


        """),
            agent=agent,
            context=context,
            asyn_execution=True

        )
