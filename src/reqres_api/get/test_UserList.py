import requests

url = "https://reqres.in/api/users?page=2"

# using request i can verify API
response = requests.get(url)
print(response)
print(response.content)
print(response.headers)



