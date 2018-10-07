import requests
import os
import json

# Site Based requests
url = "https://api.wpengineapi.com/v0/sites"
response = requests.get(url,
    auth=requests.auth.HTTPBasicAuth(
    os.environ['WPENGINE_USER_ID'],
    os.environ['WPENGINE_PASSWORD']))

data = json.loads(response.content)

for key  in data['results']:
    print("Site ID: " + key['id']) # Site ID
    print("Site Name: " + key['name']) # Site name
    for install in key['installs']:
        print("Install ID: " + install['id'])
        print("Install: " + install['name'])
    print("")
