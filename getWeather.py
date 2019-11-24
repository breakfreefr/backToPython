#!python3

'''
Gets the weather from the openweather https://openweathermap.org/ 
using the api to specify a city and get reply in json format

nb: api key stored in different directory in a json file and loaded when program run
along with the cities and the cityId 

{
  "key": "xxxxxxxxxxxxxxxxxxxx",
  "cities": {
    "York": "2633352",
    "Geneva": "6458784"
  }
}


'''
import sys
import json
import requests
import time

def getKeyAndCities():

  scriptpath = sys.path[0]
  keysrelpath = '../keys/openweather.json'
  keypath = scriptpath + '/' + keysrelpath

  f=open(keypath)
  j=f.read()
  f.close()
  jdict = json.loads(j)
  apikey = jdict["key"]
  citiesList = jdict["cities"]
  return apikey, citiesList

def getWeather(apikey, cityId):

  #print("https://api.openweathermap.org/data/2.5/weather?id=" + cityId + "&units=metric&appid=" + apikey)
  r = requests.get("https://api.openweathermap.org/data/2.5/weather?id=" + cityId + "&units=metric&appid=" + apikey)
  #print(r.content)
 # weatherDict = json.loads(r.content)
  weatherDict = r.json()
  if r.status_code == 200:  
    temperature = round(weatherDict["main"]["temp"], 1)
    weatherDescription = weatherDict["weather"][0]["description"]

    timezoneDelta = weatherDict['timezone']
    sunrise = time.ctime(weatherDict['sys']['sunrise'] + timezoneDelta)
    sunset = time.ctime(weatherDict['sys']['sunset'] + timezoneDelta)
    print(sunrise, sunset)
  
  else:
    print('error from server', r.status_code)
    exit(1)

  return temperature, weatherDescription


def main():

  (apikey, cities) = getKeyAndCities()
  for city in cities:
    cityid = cities[city]
    print(city)
    print(getWeather(apikey,cityid))
    print()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()