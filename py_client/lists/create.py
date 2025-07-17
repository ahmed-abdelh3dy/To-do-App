import requests


endpoint = 'http://127.0.0.1:8000/auth/lists'

data = {
    'title':'create list one',
    'deadline':'2025-10-10'
}

access = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyNzU5MjM5LCJpYXQiOjE3NTI2NzI4MzksImp0aSI6ImQ5OGExY2QxMTZlNTQ3ZmRiZDI4OTgzZTBjYmY1MmJhIiwidXNlcl9pZCI6M30.yxVXgUghek0argsSruhjoFPYCJLEMXeTM5SIX4UURO8'

get_response = requests.get(endpoint  , data=data )
print(get_response.json())