import requests

# endpoint = "https://httpbin.org/status/200"
#endpoint = "https://httpbin.org/anything"
endpoint = " http://localhost:8000/api/" #http://127.0.0.1:8000/

get_response = requests.get(endpoint,json={"query":"hello API"})
print(get_response.text)
print (get_response.json()['message'])
# print (get_response.status_code)