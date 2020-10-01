import requests


def get_languages():
    url = "https://microsoft-azure-translation-v1.p.rapidapi.com/GetLanguagesForTranslate"

    headers = {
        'x-rapidapi-host': "microsoft-azure-translation-v1.p.rapidapi.com",
        'x-rapidapi-key': "6923311cd5mshf40c236972f983dp1ac38ajsnbd57f09a852e"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

def get_translation(translate_text):
    url = "https://microsoft-azure-translation-v1.p.rapidapi.com/translate"
    text = translate_text
    querystring = {"from":"ja","to":"en","text":text}

    headers = {
        'x-rapidapi-host': "microsoft-azure-translation-v1.p.rapidapi.com",
        'x-rapidapi-key': "6923311cd5mshf40c236972f983dp1ac38ajsnbd57f09a852e",
        'accept': "application/json"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
def get_transliteration():
    pass
    
get_translation()
get_languages()