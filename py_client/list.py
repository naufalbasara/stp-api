import requests

endpoint = "http://localhost:8000/api/products/"
get_req = requests.get(endpoint)
print(get_req.json())