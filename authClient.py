# -*- coding: utf-8 -*-
from requests.auth import HTTPDigestAuth
from requests.auth import HTTPBasicAuth
import requests
import json

url = 'http://192.168.0.161:3000/login'
username = "Ricky"
password = "qjZq6EL8Ua5mGJfv"
basic = HTTPBasicAuth(username, password)
response = requests.post(url, auth=basic)
token = json.loads(response.content.decode("utf8"))["token"]
print(token)

urlget='http://192.168.0.161:3000/dataserver'
headerget={'Content-Type':'application/json', 'x-access-tokens':token}
dataGet=requests.get(urlget, headers=headerget)
print(dataGet.content.decode("utf8"))
