import requests
import json

objects =	{
  "tree": "tree",
  "stop sign": "stop sign"
}
objects["pole"] = "pole"


urlAnalyze = "https://canadacentral.api.cognitive.microsoft.com/vision/v1.0/analyze"

querystring = {"visualFeatures":"Tags", "language":"en"}

headers = {
    'Ocp-Apim-Subscription-Key': "dc97ef487b364479b29d5f98e017c28e",
    'Content-Type': "application/octet-stream"
    }

data = open('/Users/hadeelelmadhoon/Documents/STOP_sign.jpg', 'rb').read()
responseAnalyze = requests.request("POST", urlAnalyze, headers=headers, data=data, params=querystring)

result = json.loads(responseAnalyze.text)

for i in range(len(result['tags'])):
    if result['tags'][i]['name'] in objects:
        print(result['tags'][i]['name'] + " watch out")
