import requests
import re

class TranslateText:
    def translate(targetlanguage, text):
        #Using Python for Text Translation with Microsoft Cognitive Services
        # Specify the subscription Key
        subscriptionKey = "a710d487ff024128a1572ffbd3e0bc60"
        #Specify URLs for Cognitive Services - Translator Text API
        translateUrl = 'https://api.microsofttranslator.com/v2/http.svc/Translate'
        cognitiveServiceUrl = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'
        # Request Access Token
        requestHeader = {'Ocp-Apim-Subscription-Key': subscriptionKey}
        responseResult = requests.post(cognitiveServiceUrl, headers=requestHeader)
        token = responseResult.text
        # Specify source language
        srcLanguage = "en"
        # Define Parameters
        params = {'appid': 'Bearer '+token, 'text': text, 'from': srcLanguage, 'to': targetlanguage}
        requestHeader = {'Accept': 'application/xml'}
        # Invoke Cognitive Services to perform translation
        responseResult = requests.get(translateUrl, params=params, headers=requestHeader)

        result = re.search('<string xmlns="http://schemas.microsoft.com/2003/10/Serialization/">(.*)</string>', responseResult.text)
        if result:
            translatedText = result.group(1)
            return translatedText
        return ""
