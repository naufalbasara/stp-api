import requests

endpoint = "http://localhost:8000/api/products/1"
get_req = requests.get(endpoint)
print(get_req.json())