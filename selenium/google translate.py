"""https://rapidapi.com/hub
    fb login
"""

import requests

to_translate = input("Text to translate? ")

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

DETECT_BASE_URL = 'https://google-translate1.p.rapidapi.com/language/translate/v2/detect'
TRANSLATE_BASE_URL = 'https://google-translate1.p.rapidapi.com/language/translate/v2'


payload = f"q={to_translate}&target=bg"   #text and lang


HEADERS = {
    "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
    "X-RapidAPI-Key": "b86174402cmsh86154b8944cd90bp18e9b1jsn34de4180e9a7",
   'content-type': "application/x-www-form-urlencoded"
   }

response = requests.post(TRANSLATE_BASE_URL,data=payload.encode('utf-8'), headers=HEADERS).json()

#print(response.json())
translate = response["data"]["translations"][0]["translatedText"]
print(translate)