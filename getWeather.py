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
import json
import requests

def getKeyAndCities():
  f=open('../keys/openweather.json')
  j=f.read()
  f.close()
  #print(j)
  jdict = json.loads(j)
  apikey = jdict["key"]
  citiesList = jdict["cities"]
  return apikey, citiesList

def getWeather(apikey, cityId):

  #print("https://api.openweathermap.org/data/2.5/weather?id=" + cityId + "&appid=" + apikey)
  r = requests.get("https://api.openweathermap.org/data/2.5/weather?id=" + cityId + "&appid=" + apikey)
  #print(r.content)
  weatherDict = json.loads(r.content)
  temperature = round(weatherDict["main"]["temp"] - 273,1)
  return temperature


def main():

  (apikey, cities) = getKeyAndCities()
  for city in cities:
    cityid = cities[city]
    print(city, getWeather(apikey,cityid), 'C')
    #t = getWeather(apikey,cityid)
    #print(t)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()