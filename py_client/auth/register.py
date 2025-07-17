import requests


endpoint = 'http://127.0.0.1:8000/auth/register'

data = {
    'username':'ahmed4',
    'email':'ahh@aa.aa',
    'password':'password'
}

get_response = requests.post(endpoint  , data=data )
print(get_response.json())