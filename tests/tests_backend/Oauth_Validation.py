import requests
import jsonpath


def test_Oauth():
    token_url = "http://thetestingworldapi.com/Token"
    data = {'grant_type': 'password', 'username': 'admin'}
    response = requests.post(token_url, data)
    token_value = jsonpath.jsonpath(response.json(), 'access_token')
    auth = {'Authorization': 'Brearer' + token_value[0]}
    APU_URL = "http://thetrstingworldapi.com/api/StDetails/1104"
    response = requests.get(APU_URL, headers=auth)
    print(response.text)

