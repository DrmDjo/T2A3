import requests

url = "https://newsapi.org/v2/top-headlines"

querystring = {"country":"jp"}

headers = {
    'x-api-key': "2d2aae6c9cc64cd0a10af6ffb26b8927"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


