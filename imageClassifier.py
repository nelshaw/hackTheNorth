import requests
import json

url = "https://canadacentral.api.cognitive.microsoft.com/vision/v1.0/analyze"

querystring = {"visualFeatures":"Tags","language":"en"}

headers = {
    'Ocp-Apim-Subscription-Key': "dc97ef487b364479b29d5f98e017c28e",
    'Content-Type': "application/octet-stream"
    }
data = open('/Users/hadeelelmadhoon/Documents/tree.jpg', 'rb').read()
response = requests.request("POST", url, headers=headers, data=data, params=querystring)

result = json.loads(response.text)

for i in range(len(result['tags'])):
    if result['tags'][i]['name'] == "tree":
        print("Tree! Watch out")

