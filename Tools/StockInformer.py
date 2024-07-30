from langchain.tools import tool
import json
import os
import requests

class stock_informer:
    @tool("Get the information about stock from the ticker symbol of the stock")
    def get_information(query):
        """
        Gather the information about the stocks and return it.
        """
        url='https://financialmodelingprep.com/api/v3/profile'
        payload=json.dumps({'symbol':query})
        header={'apikey':os.environ['FINANCIAL_MODELLING_PREP_API_KEY']}
        response=requests.request("POST",url,headers=header,payload=payload)
        return response.json().pop('image')
