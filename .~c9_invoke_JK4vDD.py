import requests
import json
import config


# API call to Yahoo Japan Web Api and transliterate given text and copy into JSON
def get_transliteration(to_translit):

    url = 'http://jlp.yahooapis.jp/FuriganaService/V1/furigana'
    text = to_translit
    querystring = {'appid':config.yahoo_user_id, 'sentence':text,'format':'r'}

    headers = {
        'host': "jlp.yahooapis.jp"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #print(response.text)
        
    translit_text= response.text
   
    #trans_dict = json.loads(translit_text)
    #translation = json.loads(trans_dict)
    print(translit_text)
    #translation = trans_dict['data']['translation']
   #return translation
    
    
get_transliteration("ハロウィン")