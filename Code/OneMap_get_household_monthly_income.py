import pandas as pd
import json
import requests
import csv
import json
import datetime


df = pd.read_csv('planning_area_list_2022.csv')
# Remove the first row as it is not relevant
df = df.tail(-1) 

# insert your own API key
Authorization_key = "Insert your API key"

headers = {'Content-Type': 'application/json',
           'Authorization': Authorization_key,
           'User-Agent': 'Mozilla/5.0'}


def get_data(url):

    response = response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

# for loop to call onemap API with the planning areas gotten from previous list   
# take note that onemap API is updated every 5 years hence, we are using 2020 data
for planning_area in df['pln_area_n']:
    url = f"https://www.onemap.gov.sg/api/public/popapi/getHouseholdMonthlyIncomeWork?planningArea={planning_area}&year=2020"
    data_info = get_data(url)
    if data_info is not None:
        print("Success! json dataset to convert to csv is embedded in data_info['Result']")   
    else:
        print('[!] Request Failed')

    #flatten nested data in json file
    from pandas.io.json import json_normalize
    data = data_info
    print(data_info)
    flattendata = json_normalize(data)
    flattendata.to_csv('household_monthly_income_' + '2020' + '.csv', mode='a' , index=False)