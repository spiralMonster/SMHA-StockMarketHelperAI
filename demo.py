import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()
url="https://www.searchapi.io/api/v1/search"
params = {
  "engine": "google",
  "q": "Top 5 stocks in India under 5000 RS in financial and technical services",
  "api_key":os.environ['SEARCH_API_KEY']
}

response = requests.get(url, params = params)

if "organic_results" in response.json():
    data=[]
    results=response.json()['organic_results']
    for result in results[:5]:
        try:
            data.append("\n".join([
                f"Title: {result['title']}",
                f"Link: {result['link']}",
                f"Snippet: {result['snippet']}",
                "\n---------------------------"
            ]))
        except KeyError:
            next
    print("\n".join(data))

