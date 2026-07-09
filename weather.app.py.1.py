import requests 
import json 
import os

city = input("Enter the name of the city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY=b13989793f184149a9114538230103&q={city}"


r = requests.get(url)
#print(r.text)
wdic =  json.loads(r.text)
w = wdic["current"]["temp_c"]

os.system(f"say 'The current weather in {city} is {w} degrees'")