import requests
import json

import io
import os
import config

#Delete file on start up.
def delete_news_JSON():
    if os.path.exists("news_data.json"):
        os.remove("news_data.json")
    else:
        #print("The file does not exist")
        pass

# API call to News Api and copy into JSON
def write_news():
    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str

    url = "https://newsapi.org/v2/top-headlines"

    querystring = {"country":"jp","category":"technology"}

    headers = {
        'x-api-key': config.news_api_key
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
    
delete_news_JSON()
write_news()
read_news()