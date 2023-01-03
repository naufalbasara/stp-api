import requests

endpoint = "http://localhost:8000/api/products/1/update/"
data = {
    'name' : 'e-scooter'
}
get_req = requests.put(endpoint, json = data)
print(get_req.json())