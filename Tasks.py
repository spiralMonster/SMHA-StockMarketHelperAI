from crewai import Task
from textwrap import dedent
import datetime


class StockMarketHelperTasks:

    def StockFinderTask(self, agent, location, stock_type, amount):
        return Task(
            description=dedent(f'''
            
            **Task**:Find top 5 stocks in which the agent can invest depending upon the current scenario.
            
            **Description**:
                           *You have to search top 5 stocks depending upon the current scenario and user preferences from 
                           the Internet.
                           
                           *Then get the ticker symbols for these stocks.
                           
                           *Get information about these stocks using the ticker symbols obtained from the previous task.
                           
                           *Provide the information gathered about the stocks in a bulletin form.You should include this
                            information in the expected output format as provided.
                           
                            *You have to provide a detail explanation about the stocks using their names from internet.
                            It is expected from you to add answers to these questions in your explanation:
                            
                                  *How does the company makes money?
                                  *Are its products or services in demand?
                                  *How as the company performed in the past?
                                  *Are talented,experienced managers in charge?
                                  *Is the company positioned for growth and profitability?
                                  *How much debt does the company have?
                                  
                            *Try to include the reviews about the stock using the ticker symbols.
                            
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
                
                **PRICE OF THE STOCK** :
                
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

    def StockAnalystTask(self, agent, location, time_range, context: list):
        return Task(
            description=dedent(f'''
            **Task** : Gather news which can affect the stock prices.
            **Description** : Provide a detailed explanation in the form of bulletin that how those news will affect the
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
                              
            **Parameters** : You can use the following parameters to gather the news articles:
                             [LOCATION]: {location}
                             [TIME RANGE]: {time_range}
            '''),

            expected_output=dedent(f'''
                       Provide at least 3-5 news and how do they affect the stock with proper explanation.
                       
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
                        **TASK**: Predict the profit or loss the user would make.
                        
                        **Description**: You have to analyse the historical data regarding the stocks and predict whether 
                                         the user makes loss or profit and how much loss or profit the user can
                                         made at different timestamps.
                                         So you have to provide that information for every month upto 3 months.
                                         You can predict the profit/loss using the following features:
                                                * Data of observation
                                                * Opening price
                                                * Highest price during trading day
                                                * Lowest price during trading day
                                                * Close price
                                                * Close price adjusted for stock splits and dividends
                                                * Number of shares traded during trading day
                                                * News affecting the stocks
                                                
                                        Here Close price is the dependent feature.
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
                      **Task**: Analyse the historical data about stocks using their ticker symbol.
                      **Description**: You have to analyse the historical data about the stocks and provide various insights about
                                it at every one month before upto 3 months back.You can provide insights on the following topics in bulletin form:
                                
                                        * Opening price
                                        * Highest price during trading day
                                        * Lowest price during trading day
                                        * Close price
                                        * Volume
                                        
                                Compare these values with their current values and also provide a detailed explanation about it.
                                
                      **Parameters**:
                        [Current Date]: {datetime.date.today().strftime("%d/%m/%Y")}
                    '''

            ),
            agent=agent,
            context=context,
            asyn_execution=True

        )
