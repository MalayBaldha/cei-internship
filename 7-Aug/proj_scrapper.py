from date_gen import date_gen
import requests
import json
from PIL import Image
from io import BytesIO  
import pandas as pd

url = "https://vegetablemarketprice.com/api/dataapi/market/gujarat/daywisedata?date="

header = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Referer": "https://vegetablemarketprice.com/market/himachalpradesh/today",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }

date_list = date_gen( [1,5,2024], [30,6,2024])

final_data = []

for date in date_list:
    data = requests.get(url+date, headers = header)
    js = json.loads(data.text)
    
    print(date)
    arr = []
    for api in js["data"]:

        id = str(api["id"])
        name = str(api["vegetablename"])
        whole_price= str(api["price"])
        retail_price = str(api["retailprice"])
        shoping_mall_price = str(api["shopingmallprice"])
        unit = str(api["units"])
        image = "https://vegetablemarketprice.com/" + str(api["table"]["table_image_url"])

        response = requests.get(image)
        img = Image.open(BytesIO(response.content))

        new_js = {
            "Date": date,
            "Id": id,
            "Vegetable Name": name,
            "Wholesale Price": whole_price,
            "Retail Price": retail_price,
            "Shopping Mall Price": shoping_mall_price,
            "Units": unit,
            "Image":img,
        }
        arr.append(new_js)

    final_data.extend(arr)
 
    
df = pd.DataFrame(final_data)
df.to_csv("Output2.csv")

