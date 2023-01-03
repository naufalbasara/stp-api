import requests

pk = input("Input product id that you want to delete: ")
while pk != int(pk):
    pk = input("Input valid product id that you want to delete: ")
    if pk == int(pk):
        pk = int(pk)
        break

endpoint = "http://localhost:8000/api/products/1/delete"
get_req = requests.get(endpoint)
print(get_req.json())