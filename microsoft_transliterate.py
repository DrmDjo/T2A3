import requests, uuid, json


# API call to Microsoft Azure Translate to transliterate text and copy into JSON
def get_transliteration(to_translit):
    
    text = to_translit
    
    # Add your subscription key and endpoint
    subscription_key = "71f480298d394bf89b0a987c4b4efa0c"
    endpoint = "https://api.cognitive.microsofttranslator.com"
    
    path = '/transliterate'
    constructed_url = endpoint + path
    
    params = {
        'api-version': '3.0',
        'language': 'ja',
        'fromScript': 'Jpan',
        'toScript': 'Latn'
    }
    constructed_url = endpoint + path
    
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    
    
    body = [{
        'text': text
    }]
    
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    
    translit_json = json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
    

        
    
   
    trans_dict = json.loads(translit_json)
    
    #print(trans_dict)
    transliteration = trans_dict[0]['text']
    print(transliteration)
    
    return transliteration
    
    
get_transliteration("電話番号")