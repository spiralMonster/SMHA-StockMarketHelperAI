from langchain.tools import tool
import os
import json
import requests

class stock_history:
    @tool("Get the historical data about stocks from their ticker symbol")
    def get_history(query):

