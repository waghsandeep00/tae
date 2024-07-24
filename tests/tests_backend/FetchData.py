import requests
import json
import jsonpath


def test_getdata():
    url = "https://reqres.in/api/users?page=2"

    response = requests.get(url)
    print(response)

    print(response.content)
    print(response.headers.get("date"))
    statuscode = response.status_code
    print(response.status_code)
    assert statuscode == 200


# fetch any specific content from json content

    json_content = json.loads(response.text)
    pages = jsonpath.jsonpath(json_content, 'total_pages')
    assert pages[0] == 2


# parsh all Firstname data from json response
    for i in range(0, 3):
        first_name = jsonpath.jsonpath(json_content, 'data[' + str(i) + '].first_name')
        print((first_name[0]))
# parsh specific Firstname data from json response
    first_name = jsonpath.jsonpath(json_content, 'data[1].first_name')
    print(first_name[0])


