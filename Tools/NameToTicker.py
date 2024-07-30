from langchain.tools import tool
import json
import os
import requests

class name_to_ticker_symbol:
    @tool("Get the ticker symbols from the name of the stock")
    def get_symbol(query):
        """
        Get the ticker symbol from the name of the stock and return it
        """
        url='https://financialmodelingprep.com/api/v3/search-ticker?'
        payload=json.dump({"query":query,'limit':1})
        header={
            'apikey':os.environ['FINANCIAL_MODELLING_PREP_API_KEY']
        }
        response=requests.request("POST",url,headers=header,payload=payload)
        return response.json()['symbol']