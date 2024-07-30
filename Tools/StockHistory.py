from langchain.tools import tool
import os
import requests


class stock_history:
    @tool("Get the historical data about stocks from their ticker symbol")
    def get_history(query):
        """
        Get the historical data about the stock using their ticker symbols for past 6 months.
        """
        url='https://api.twelvedata.com/time_series'
        headers={
            'symbol':query,
            'interval':"6month",
            'apikey':os.environ['TWELVE_DATA_API_KEY']
        }
        response=requests.request("GET",url,headers=headers)

        if response.json()['values']:
            results=response.json()['values']

        else:
            print("Sorry we are unable to process your request")

        return results








