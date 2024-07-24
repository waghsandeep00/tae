import requests
import json
import jsonpath


def test_oauth():
    token_url = "https://thetestingworldapi.com/Token"
    data = {'grant_type': 'Password', 'Username': 'xyx', 'Password': 'test@123'}
    response = requests.post(token_url, data)
    token_value = jsonpath.jsonpath(response.json(), 'access_token')

    auth = {'Autorisation': 'Brearer' + token_value(0)}
    API_URL= "https://thetestingworldapi.com/api/StDetails/154679"
    response = requests.get(API_URL)
    print(response.text)





