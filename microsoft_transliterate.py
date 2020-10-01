import requests, uuid, json


# API call to Microsoft Azure Translate to transliterate text and copy into JSON
def get_transliteration(to_translit):
    
    text = to_translit
    #encode_text = text.encode('utf-8')
    
    # Add your subscription key and endpoint
    subscription_key = "71f480298d394bf89b0a987c4b4efa0c"
    endpoint = "https://api.cognitive.microsofttranslator.com"
    
    path = '/transliterate'
    constructed_url = endpoint + path
    
    params = {
        'api-version': '3.0',
        'language': 'ja',
        'fromScript': 'Jpan',
        'toScript': 'latn'
    }
    constructed_url = endpoint + path
    
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    
    # You can pass more than one object in body.
    body = [{
        'text': text
    }]
    
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    
    print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))
    

        
    #translit_text= response.text
   
    #trans_dict = json.loads(translit_text)
    #translation = json.loads(trans_dict)
    #print(translit_text)
    #translation = trans_dict['data']['translation']
  #return translation
    
    
get_transliteration("こんにちは")