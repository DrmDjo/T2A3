import requests
import re


def get_translation(translate_text):
    
    text = translate_text
    encode_text = text.encode('utf-8')
    
    url = "https://microsoft-azure-translation-v1.p.rapidapi.com/translate"
    
    querystring = {"from":"ja","to":"en","text":encode_text}

    headers = {
        'x-rapidapi-host': "microsoft-azure-translation-v1.p.rapidapi.com",
        'x-rapidapi-key': "6923311cd5mshf40c236972f983dp1ac38ajsnbd57f09a852e",
        'accept': "application/json"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)


    
    #print(response.text)
    output = response.text
    #Strip HTML Tags
    get_html_config = re.compile('<.*?>')
    just_translated_text = re.sub(get_html_config, '', output)
    
    #print(just_translated_text)
    return just_translated_text
    

    
#get_translation("自分で書いて、自分で買って、自分で使ってます")
#get_languages()
