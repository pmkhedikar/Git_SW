import requests
import json
import jsonpath

url = "https://reqres.in/api/users"


# Loading the json request file & creating the json request
file = open(r"C:\Users\paragk1\PycharmProjects\Git_SW\src\reqres_api\data\CreateUser.json",'r')
json_input = file.read()
request_json = json.loads(json_input)
# print(json_input)
# print(request_json)

#Creating a post request with json input
post_response = requests.post(url,request_json)
print(post_response)

#validating the response code
assert post_response.status_code == 201

# print(post_response.content)  #Getting the request content
# print(post_response.headers)  #Getting the request header
# print(post_response.headers.get('Content-Length'))   # Getting particular content value in header

#Getting the response in json
post_response_json = json.loads(post_response.text)
print(post_response_json)

#Pick id using json path
id = jsonpath.jsonpath(post_response_json,'id')
print(id)
print(id[0])