
import requests
import os
import json

# Install Based Request
url = "https://api.wpengineapi.com/v0/installs"

response = requests.get(url,
    auth=requests.auth.HTTPBasicAuth(
    os.environ['WPENGINE_USER_ID'],
    os.environ['WPENGINE_PASSWORD']))

data = json.loads(response.content)
account_id = data['results'][0]['account']['id']

print("Account ID: " + account_id)
print("")

for key in data['results']: #Iterate over each install
    print("Install: " + key['name'])
    # install_id is used for requests to that specific install. We'll use it later on.
    install_id = key['id']
    print("Environment: " + str(key['environment']).lower()) #If its a single envrionment site it'll retuurn None type object
    print("Primary Domain: " + key['primary_domain'])
    print("PHP Version: " + key['php_version'])
    print("") # Just separate things out a bit in output.
