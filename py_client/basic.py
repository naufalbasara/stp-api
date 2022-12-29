import requests
endpoint = "http://localhost:8000"

data = requests.get(endpoint)
print(data)