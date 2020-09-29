import requests


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
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    text = to_translate
    payload = f"source=en&q={text}&target=ja"
    headers = {
        'x-rapidapi-host': "google-translate1.p.rapidapi.com",
        'x-rapidapi-key': "6923311cd5mshf40c236972f983dp1ac38ajsnbd57f09a852e",
        'accept-encoding': "application/gzip",
        'content-type': "application/x-www-form-urlencoded"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    #print(response.text)
    return response.text
#get_translation()
#get_languages()