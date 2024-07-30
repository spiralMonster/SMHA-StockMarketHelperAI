from langchain.tools import tool
import requests
import os
from bs4 import BeautifulSoup


class stock_reviewer:
    @tool("Get reviews about the stock from its ticker symbol")
    def get_review(query):
        """
        Gather the reviews about the stocks of the company across different platforms and return it.
        """
        num_of_reviews=5
        url='https://reviewindexapi.datashake.com/profiles'
        params={
            'api_key':os.environ["DATASHAKE_API_KEY"],
            'ticker_symbol':query
        }
        response=requests.get(
            url=url,
            params=params
        )
        if "success"=="true":
            results=response.json()['results']['profiles']
            review_urls=[]
            for result in results[:num_of_reviews]:
                try:
                    review_urls.append(result['url'])
                except KeyError:
                    print("Sorry we are unable to fetch your urls")
        else:
            print("Sorry we are unable to process your request")

        reviews=[]
        for u in review_urls:
            text=requests.get(u)
            if text.status_code==200:
                soup=BeautifulSoup(text.content,'lxml')
                reviews.append(soup.get_text(separator='\n',strip=True))
            else:
                print("Sorry unable to fetch your url")


        return reviews
