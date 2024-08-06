import requests
import time
import json
import pandas as pd

new_json = {"time":[], "latitude":[], "longitude":[]}
url = "http://api.open-notify.org/iss-now.json"

i = 1
while i<=100:
    # get data from the url
    try:
        data = requests.get(url)
        print(f"Step {i}/100")
        i += 1
        # convert data to json data
        json_data = json.loads(data.text)
        lat = json_data["iss_position"]["latitude"]
        long = json_data["iss_position"]["longitude"]
        timestamp = json_data["timestamp"]

        new_json["time"].append(timestamp)
        new_json["latitude"].append(lat) 
        new_json["longitude"].append(long)
    
    except:
        print("Connection break. Sleeping for 10 sec...")
        time.sleep(10)
        print("Continuing...")
        continue

df = pd.DataFrame(new_json)
df.to_csv("output.csv")