import requests
import json

import io

def write_kanji():
    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str
    
    
    url = "https://kanjialive-api.p.rapidapi.com/api/public/kanji/all"
    
    querystring = {"grade":"1"}
    #querystring = {}
    
    
    headers = {
        'x-rapidapi-host': "kanjialive-api.p.rapidapi.com",
        'x-rapidapi-key': "6923311cd5mshf40c236972f983dp1ac38ajsnbd57f09a852e"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    #print(response.text)
    
    kanji_list = json.loads(response.text)
    
    with io.open("kanji_data.json","w", encoding='utf8') as data_file:
        str_ = json.dumps(kanji_list,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        data_file.write(to_unicode(str_))
    
    
    # for kanji in kanji_list:
    #     print(kanji["kanji"]["character"])
    
def read_kanji():
    with io.open("kanji_data.json") as data_file:
        data_loaded = json.load(data_file)

   # print(data_loaded)
    

write_kanji()
read_kanji()