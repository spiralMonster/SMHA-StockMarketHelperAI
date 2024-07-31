from langchain.tools import tool
import os
import requests


class stock_history:
    @tool("Get the historical data about stocks from their ticker symbol")
    def get_history(query):
        """
        Get the historical data about the stock using their ticker symbols for past 6 months.
        """
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={query}&apikey={os.environ['ALPHA_VANTAGE_API_KEY']}"
        num_of_months=6
        ind=0
        response=requests.get(url)
        if response.json() is not None:
            results=response.json()['Monthly Adjusted Time Series']
            data=[]
            for dates,values in results.items():
                try:
                    data.append("\n".join([
                        f"Date: {dates}",
                        f"Opening Price of Stock: {values['1. open']}",
                        f"Closing Price of Stock: {values['4. close']}",
                        f"Highest Price of Stock: {values['2. high']}",
                        f"Lowest Price of Stock: {values['3. low']}",
                        f"Adjusted Closing Price of Stock: {values['5. adjusted close']}",
                        f"Volume of Stock: {values['6. volume']}",
                        f"\n-------------------------------------"

                    ]))
                    ind+=1
                except KeyError:
                    print("Sorry an unexpected error occur!!!")

                if ind==num_of_months:
                    break

            return "\n".join(data)

        else:
            print("Sorry not able to process your request right now.")











