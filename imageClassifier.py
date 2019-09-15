import requests
import json
from translateText import TranslateText
import urllib.request

objects =	{
  "tree": "tree",
  "stop sign": "stop sign",
  "fire hydrant": "fire hydrant",
  "person": "person"
}

urlAnalyze = "https://canadacentral.api.cognitive.microsoft.com/vision/v1.0/analyze"

querystring = {"visualFeatures":"Tags", "language":"en"}

headers = {
    'Ocp-Apim-Subscription-Key': "dc97ef487b364479b29d5f98e017c28e",
    'Content-Type': "application/octet-stream"
    }

class ImageClassifier:
  def findTags(targetlanguage):
    urllib.request.urlretrieve('http://raspberrypi.local:5000/data/image.jpg', 'data/image.jpg')
    
    data = open('data/image.jpg', 'rb').read()
    # data = open('C:/Users/Nadeen Elshawish/source/hackTheNorth/data/frame655.jpg', 'rb').read()
    responseAnalyze = requests.request("POST", urlAnalyze, headers=headers, data=data, params=querystring)

    result = json.loads(responseAnalyze.text)
    resultString=""
    for i in range(len(result['tags'])):
        if result['tags'][i]['name'] in objects:
          resultString += result['tags'][i]['name'] + " up ahead, watch out ..."
    print(resultString)
    str = TranslateText.translate(targetlanguage=targetlanguage, text=resultString)
    print(str)
    return str
