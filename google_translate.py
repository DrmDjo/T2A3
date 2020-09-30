import requests
import json
import config


# API call to Google Translate Api and translate given text and copy into JSON
def get_translation(to_translate):

    url = "https://google-translate20.p.rapidapi.com/translate"
    text = to_translate
    querystring = {"sl":"ja","text":text,"tl":"en"}

    headers = {
        'x-rapidapi-host': "google-translate20.p.rapidapi.com",
        'x-rapidapi-key': config.google_api_key
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #print(response.text)
        
    translated_text= response.text
   
    trans_dict = json.loads(translated_text)
    #translation = json.loads(trans_dict)
    #print(trans_dict['data']['translation'])
    translation = trans_dict['data']['translation']
    return translation
    
    
#get_translation("ハロウィン")
