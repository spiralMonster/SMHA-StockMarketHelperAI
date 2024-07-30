from langchain.tools import tool
import os
import json
import requests
import datetime
from dateutil.relativedelta import relativedelta

class stock_history:
    @tool("Get the historical data about stocks from their ticker symbol")
    def get_history(query):
        """
        Gather the historical data about the stock market and return it.
        """
        current_date=datetime.date.today()
        prev_date=current_date-relativedelta(months=6)
        url="https://api.marketdata.app/v1/stocks/candles"
        headers={
            'Accept':'application/json',
            'Authorization':f"Bearer {os.environ['MARKET_DATA_API_KEY']}"
        }
        payload=json.dumps(
            {
                'resolution':'monthly',
                'symbol':query,
                'from':prev_date,
                'to':current_date

            }
        )
        response=requests.request("GET",url,headers=headers,payload=payload)
        if response.status_code in (200,203):
            results=response.json()
            return "\n".join([
                f"Open Price: {results['o']}",
                f"Highest Price: {results['h']}",
                f"Lowest Price: {results['l']}",
                f"Closing Price: {results['c']}",
                f"Volume: {results['v']}",
                "\n---------------------"
            ])

        else:
            print("Sorry we are unable to process your request!!!")


