from langchain.tools import tool
import os
import json
import requests

class search_tool:
    @tool("Search the internet")
    def search_internet(query):
        """
        Search the relevant results from the internet and return it.
        """
        top_results_to_return=6
        url = "https://www.searchapi.io/api/v1/search"
        params = {
            "engine": "google",
            "q": "Top 5 stocks in India",
            "api_key": os.environ['SEARCH_API_KEY']
        }

        response = requests.get(url, params=params)

        if "organic_results" in response.json():
            data = []
            results = response.json()['organic_results']
            for result in results[:top_results_to_return]:
                try:
                    data.append("\n".join([
                        f"Title: {result['title']}",
                        f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}",
                        "\n---------------------------"
                    ]))
                except KeyError:
                    next
            return("\n".join(data))

