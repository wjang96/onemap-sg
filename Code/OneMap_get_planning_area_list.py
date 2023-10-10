import json
import requests
import pandas as pd
import csv
import json

import datetime

# Get the current date
current_date = datetime.datetime.now()

# Subtract 1 year from the current year
one_year_ago = current_date - datetime.timedelta(days=365)

# Get the year from the result
year_minus_1 = one_year_ago.year

print(year_minus_1)
      
url = f"https://www.onemap.gov.sg/api/public/popapi/getPlanningareaNames?year={year_minus_1}"

# insert your own API key
Authorization_key = "Insert your API key"

headers = {'Content-Type': 'application/json',
           'Authorization': Authorization_key,
           'User-Agent': 'Mozilla/5.0'}

# Perform API call to get the list of planning areas dated last year
def get_data():

    response = response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
    
data_info = get_data()

if data_info is not None:
    print("Success! json dataset to convert to csv is embedded in data_info['Result']")   
else:
    print('[!] Request Failed')

#flatten nested data in json file
from pandas.io.json import json_normalize
data = data_info
flattendata = json_normalize(data)

#convert json data to .csv file, removing the index number
flattendata.to_csv('planning_area_list_' + str(year_minus_1) + '.csv', index=False)