import requests

headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUzMDk0NDQyLCJpYXQiOjE3NTMwMDgwNDIsImp0aSI6ImZlOGQxOGE1YWI5ODQ2MGY5OWY1ZWM1MmI2ZjAyMWQzIiwidXNlcl9pZCI6M30.axpkzK-Gk7uvkFYSIbk3qjUEf4c9byHLkUdRj2_L4Wo'}
endpoint = 'http://127.0.0.1:8000/lists'

data = {
    'title':'create list two',
    'deadline':'2025-10-10'
}


get_response = requests.post(endpoint  , json=data , headers = headers )
print(get_response.json())