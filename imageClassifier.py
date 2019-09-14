import requests
import json

url = "https://canadacentral.api.cognitive.microsoft.com/vision/v1.0/analyze"

querystring = {"visualFeatures":"Tags","language":"en"}

headers = {
    'Ocp-Apim-Subscription-Key': "dc97ef487b364479b29d5f98e017c28e",
    'Content-Type': "application/octet-stream"
    }
data = open('/Users/Nadeen Elshawish/source/hackTheNorth/download.jpg', 'rb').read()
response = requests.request("POST", url, headers=headers, data=data, params=querystring)

result = json.loads(response.text)

print(result)
