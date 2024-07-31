from crewai import Crew,Process
from Agents import StockMarketHelperAgents
from Tasks import StockMarketHelperTasks
from dotenv import load_dotenv
from textwrap import dedent

load_dotenv()

class StockMarketHelper:
    def __init__(self,parameters):
        self.parameters=parameters
    def run(self):
        #Agents:
        agent=StockMarketHelperAgents()

        agent_finder=agent.StockFinder()
        agent_analyser=agent.StockAnalyst()
        agent_researcher=agent.StockResearcher()
        agent_predictor=agent.StockPredictor()
        agent_reporter=agent.ReportProviderAgent()
        agent_brocker=agent.BestTimeToSellStockAgent()
        agent_reviewer=agent.StockReviewerAgent()

        #Tasks:
        task=StockMarketHelperTasks()

        task_finder=task.StockFinderTask(agent=agent_finder,
                                         location=self.parameters['location'],
                                         stock_type=self.parameters['type'],
                                         amount=self.parameters['amount'])

        task_analyser=task.StockAnalystTask(agent=agent_analyser,
                                            location=self.parameters['location'],
                                            context=[task_finder])

        task_researcher=task.StockResearcherTask(agent=agent_researcher,
                                                 context=[task_finder])

        task_predictor=task.StockPredictorTask(agent=agent_predictor,
                                               context=[task_finder,task_analyser,task_researcher])

        task_reviewer=task.StockReviewerTask(agent=agent_reviewer,
                                             context=[task_finder])

        task_brocker=task.BestTimeToSellStockTask(agent=agent_brocker,
                                                  context=[task_predictor])

        task_reporter=task.ReportProviderTask(agent=agent_reporter,
                                              context=[task_finder,task_reviewer,task_analyser,task_researcher,
                                                       task_predictor,task_brocker])

        #Crew:
        crew=Crew(
            agents=[agent_finder,agent_reviewer,agent_analyser,agent_researcher,agent_predictor,agent_brocker,
                    agent_reporter],
            tasks=[task_finder,task_reviewer,task_analyser,task_researcher,task_predictor,task_brocker,task_reporter],
            process=Process.sequential,
            full_output=False,
            verbose=False

        )

        crew.kickoff()



print(dedent('''      ---------- Welcome to our Stock Helper -------------
                     
                         Please answer the following questions:
             '''))
location=input(dedent('''*Enter your location: '''))
amount=input(dedent('''  *What is the maximum amount you can invest in stocks?: '''))
type=input(dedent('''    *What types of stock you are interested in?: '''))

params={
    'location':location,
    'amount':amount,
    'type':type
}

stock_market_helper=StockMarketHelper(params)
stock_market_helper.run()





