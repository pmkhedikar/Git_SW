import requests
import json
import jsonpath
import pytest

url = "https://reqres.in/api/users"
mainUrl ="https://reqres.in"

@pytest.mark.skip
def test_createUser():
    file = open(r"C:\Users\paragk1\PycharmProjects\Git_SW\src\reqres_api\data\CreateUser.json",'r')
    json_input = file.read()
    request_json = json.loads(json_input)

    #Creating a post request with json input & verify the response code
    post_response = requests.post(url,request_json)
    assert post_response.status_code == 201

    ##Getting the request content ,Hearder ,particular content value
    print(post_response.content)
    print(post_response.headers)
    print(post_response.headers.get('Content-Length'))

    #Getting the response in json format & fetch the particular value from JSON
    post_response_json = json.loads(post_response.text)
    id = jsonpath.jsonpath(post_response_json,'id')
    print(id[0])


def test_createUser_new():
    file = open( r"C:\Users\paragk1\PycharmProjects\Git_SW\src\reqres_api\data\CreateUser.json", 'r' )
    json_input = file.read()
    request_json = json.loads( json_input )


    # Creating a post request with json input
    post_response = requests.post( url, request_json )
    assert post_response.status_code == 201

    # Getting the response in json
    post_response_json = json.loads( post_response.text )
    name = jsonpath.jsonpath( post_response_json, 'name' )
    print(post_response_json )
    assert name[0] =='morpheus'


def test_userRegistraion():
    reqUrl = "/api/register"
    file = open(r"C:\Users\paragk1\PycharmProjects\Git_SW\src\reqres_api\data\UserRegistration.json")
    json_input = file.read()
    request_json = json.loads(json_input)

    response = requests.post(mainUrl+reqUrl,request_json)
    assert response.status_code == 200

    post_response_json = json.loads( response.text )
    id = jsonpath.jsonpath(post_response_json,'id')
    print(id[0])


# if __name__ == "__main__":
#     test_userRegistraion()