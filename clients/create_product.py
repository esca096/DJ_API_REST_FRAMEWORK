import requests

endpoint = "http://localhost:8000/api/product/"

data = {
    'name': 'MAHATMA GHANDI',
    'price': 2500,
    'description': 'CENTER CONFERENCE',
    'email': 'cicmg@gmail.com'
}

response = requests.post(endpoint, json=data)

print(response.json())

print(response.status_code)