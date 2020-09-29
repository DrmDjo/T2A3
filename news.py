import requests
import json

import io

def write_news():
    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str

    url = "https://newsapi.org/v2/top-headlines"

    querystring = {"country":"jp","category":"technology"}

    headers = {
        'x-api-key': "2d2aae6c9cc64cd0a10af6ffb26b8927"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #print(response.text)


    news_list = json.loads(response.text)
    
    with io.open("news_data.json","w", encoding='utf8') as data_file:
        str_ = json.dumps(news_list,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        data_file.write(to_unicode(str_))
    
    
    # for kanji in kanji_list:
    #     print(kanji["kanji"]["character"])
    
def read_news():
    with io.open("news_data.json") as data_file:
        data_loaded = json.load(data_file)

   # print(data_loaded)
    

write_news()
read_news()