import requests
import json
url = 'http://127.0.0.1:5000/api/user'
data = {
    'username': 'admin',
    'password': '111111',
    'email': 'admin@admin.com'
}
header = {
    'Content-Type': 'application/json'
}
r = requests.post(url, headers=header, data=json.dumps(data))
print(r.text)