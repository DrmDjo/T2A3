import requests
import json


def get_languages():
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

    headers = {
        'x-rapidapi-host': "google-translate1.p.rapidapi.com",
        'x-rapidapi-key': "6923311cd5mshf40c236972f983dp1ac38ajsnbd57f09a852e",
        'accept-encoding': "application/gzip"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

def get_translation(to_translate):

    url = "https://google-translate20.p.rapidapi.com/translate"
    text = to_translate
    querystring = {"sl":"ja","text":text,"tl":"en"}

    headers = {
        'x-rapidapi-host': "google-translate20.p.rapidapi.com",
        'x-rapidapi-key': "6923311cd5mshf40c236972f983dp1ac38ajsnbd57f09a852e"
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
#get_languages()