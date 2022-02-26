import requests
import json

api_key = '7aa8de741165466db4a46d7f162acdaa'
base_url = 'http://api.weatherbit.io/v2.0/history/airquality?'
latitude = 33.448
longitude = -112.074
start_date = '2014-01-01'
end_date = '2014-01-31'
url = base_url+f'lat={latitude}&lon={longitude}&start_date={start_date}&end_date={end_date}&tz=local&key='+api_key
page = requests.get(url)
print(page.content)