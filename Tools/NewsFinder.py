from langchain.tools import tool
import json
import os
import requests

class news_finder:
    @tool("Find the News")
    def find_news(query):
        """
        Find the relevant news articles affecting the stocks of the company.
        """
        num_of_results=5
        url='https://newsapi.org/v2/everything?'
        headers={'apiKey':os.environ['NEWS_API_KEY']}
        payload=json.dumps({'q':query})
        response=requests.request("POST",url,headers=headers,payload=payload)
        if 'articles' not in response.json():
            print("Sorry we are not able to get response for your query")
        else:
            results=response.json()['articles']
            string=[]
            for result in results[:num_of_results]:
                try:
                    string.append("\n".join([
                        f"Title: {result['title']}",
                        f"Description: {result['description']}",
                        f"Content: {result['content']}",
                        "\n------------------------"
                    ]))

                except KeyError:
                    next

            return "\n".join(string)



