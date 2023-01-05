import requests

pk = input("Input product id that you want to delete: ")
try:
    pk = int(pk)
except:
    print('input the correct number id!')
    pk=None

if pk:
    endpoint = f"http://localhost:8000/api/products/{pk}/delete"
    get_req = requests.delete(endpoint)
    print(get_req.status_code)