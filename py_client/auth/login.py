import requests


endpoint = 'http://127.0.0.1:8000/auth/login'
data = {
    'username':'ahmed3',
    'password':'password'
}

get_response = requests.post(endpoint  , data=data )
print(get_response.json())