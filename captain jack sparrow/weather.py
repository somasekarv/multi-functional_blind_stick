import requests

API_Key = "#################api key#######################"
weather_url="http://api.openweathermap.org/data/2.5/weather?q=tamilnadu&appid="
final_url = weather_url + API_Key
json_data = requests.get(final_url).json()

def temp():

   temprature= round(json_data["main"]["temp"]-273,1)
   return temprature

def des():

   description=json_data["weather"][0]["description"]
   return description

