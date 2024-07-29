from langchain.tools import tool
import os
import json
import requests

class search_tool:
    @tool("Search the internet")
    def search_internet(query):
        top_results_to_return=4
        url='https://serper.dev/search'
        payload=json.dumps({"q":query})
        headers={
            'X-API-KEY':os.environ['SERPER_API_KEY'],
            'content_type':'application/json'
        }
        response=requests.request("POST",url,headers=headers,payload=payload)
        if 'organic' not in response.json():
            print("Sorry we cannot found the results of your query!!")
        else:
            results=response.json()['organic']
            string=[]
            for result in results[:top_results_to_return]:
                try:
                    string.append("\n".join(
                        [f"Title: {result['title']}",
                         f"Links: {result['link']}",
                         f"Snippet: {result['snippet']}",
                         "\n---------------"
                        ])
                    )
                except KeyError:
                    next

            return "\n".join(string)




