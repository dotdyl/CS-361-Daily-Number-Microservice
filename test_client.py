import requests, json

url = "http://127.0.0.1:6000/daily_number"

response = requests.get(url)

print(json.dumps(response.json(), indent = 4))