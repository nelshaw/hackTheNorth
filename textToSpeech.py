import os
import requests
import time
import sys
from xml.etree import ElementTree
from playsound import playsound
from imageClassifier import ImageClassifier

try:
    input = raw_input6
except NameError:
    pass



if sys.argv[1] == 'fr':
    language='fr'
    country='FR'
    speaker='HortenseRUS'

elif sys.argv[1] == 'en':
    language='en'
    country='US'
    speaker='Jessa24kRUS'

elif sys.argv[1] == 'es':
    language='es'
    country='ES'
    speaker='HelenaRUS'

elif sys.argv[1] == 'ko':
    language='ko'
    country='KR'
    speaker='HeamiRUS'

elif sys.argv[1] == 'ar':
    language='ar'
    country='EG'
    speaker='Hoda'

class TextToSpeech(object):
    def __init__(self, subscription_key):
        self.subscription_key = subscription_key
        self.tts = ImageClassifier.findTags(language)
        self.timestr = time.strftime("%Y%m%d-%H%M")
        self.access_token = None

    def get_token(self):
        fetch_token_url = "https://canadacentral.api.cognitive.microsoft.com/sts/v1.0/issuetoken"
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key
        }
        response = requests.post(fetch_token_url, headers=headers)
        self.access_token = str(response.text)

    def save_audio(self, language, country, speaker):
        base_url = 'https://canadacentral.tts.speech.microsoft.com/'
        path = 'cognitiveservices/v1'
        constructed_url = base_url + path
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': 'riff-16khz-16bit-mono-pcm',
            'User-Agent': 'TextToSpeechHTN'
        }
        xml_body = ElementTree.Element('speak', version='1.0')
        xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', language + '-' + country)
        voice = ElementTree.SubElement(xml_body, 'voice')
        voice.set('{http://www.w3.org/XML/1998/namespace}lang', language + '-' + country)
        languageString = language + '-' + country +', ' + speaker
        voice.set(
            'name', 'Microsoft Server Speech Text to Speech Voice (' + languageString + ')')
        voice.text = self.tts
        body = ElementTree.tostring(xml_body)

        response = requests.post(constructed_url, headers=headers, data=body)
        if response.status_code == 200:
            self.fileName = 'sample-' + self.timestr + '.wav'
            with open('sample-' + self.timestr + '.wav', 'wb') as audio:
                audio.write(response.content)
                print("\nStatus code: " + str(response.status_code) +
                    "\nYour TTS is ready for playback.\n")
        else:
            print("\nStatus code: " + str(response.status_code) +
                "\nSomething went wrong. Check your subscription key and headers.\n")
    
    def play_audio(self):
        playsound(self.fileName)
    
    def cleanup(self):
        for fname in os.listdir('.'):
        # Delete audio files except most recent one
            if fname.endswith('.wav') and fname != self.fileName:
                print("Cleaning up directory ...")
                os.remove(fname)

if __name__ == "__main__":
    if len(ImageClassifier.findTags(targetlanguage=language)) > 0:
        subscription_key = "9c32d6d1645c41bea78ae1bad878c70b"
        app = TextToSpeech(subscription_key)
        app.get_token()
        app.save_audio(language=language, country=country, speaker=speaker)
        app.play_audio()
        app.cleanup()