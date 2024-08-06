import requests
import json

# get data from the url
url = "http://api.open-notify.org/iss-now.json"
data = requests.get(url)
print(data)
print(data.text)

# convert data to json data
json_data = json.loads(data.text)
print(json_data)