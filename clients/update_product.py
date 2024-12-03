import requests

endpoint = "http://localhost:8000/api/product/1/"

data = {
    'name': 'BANQUET',
    'price': 300,
    'description': 'Full Compatment',
    'email': 'banquet@gmail.com'
}

response = requests.put(endpoint, json=data)

print(response.json())

print(response.status_code)