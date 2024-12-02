import requests

endpoint = "http://localhost:8000/api/"

data = {
    'name': 'HUIT-CLOS',
    'price': 100,
    'description': 'FULL PLACE',
}

response = requests.post(endpoint, json=data)

print(response.json())

print(response.status_code)