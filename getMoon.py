#!python3

'''
Gets the sun and moon sunrise time from here.com

nb: api key stored in ../keys/astronomy.json and loaded when program run
along with the cities and the lat and long 

note : relative path !!! needs to find absolute directory of where the program is!

{
    "comment" : "astronomy forecast",
    "APP_ID" : "xxxxxxxxxxxx",
    "APP_CODE" : "yyyyyyyyyyyyy",
    "APP_URL" : "https://weather.api.here.com/weather/1.0/report.json",
    "PRODUCT" : "forecast_astronomy",
    "city": "Geneva", 
}

api details : https://developer.here.com/api-explorer/rest/auto_weather/weather-forecast-7days-astronomy

https://weather.cit.api.here.com/weather/1.0/report.json?product=forecast_astronomy\
&name=Geneva\
&app_id=DemoAppId01082013GAL\
&app_code=AJKnXv84fjrb0KIHawS0Tg\

response :

{
  "astronomy": {
    "astronomy": [
      {
        "sunrise": "7:50AM",
        "sunset": "4:54PM",
        "moonrise": "7:19AM",
        "moonset": "5:06PM",
        "moonPhase": -0.006,
        "moonPhaseDesc": "New moon",
        "iconName": "cw_new_moon",
        "city": "Lancy",
        "latitude": 46.2,
        "longitude": 6.13,
        "utcTime": "2019-11-26T00:00:00.000+01:00"
      },
      ANOTHER 6 ELEMENTS HERE
      }
    ],
    "country": "Switzerland",
    "state": "Geneva",
    "city": "Canton of Geneva",
    "latitude": 46.19673,
    "longitude": 6.11044,
    "timezone": 1
  },
  "feedCreation": "2019-11-26T20:59:50.314Z",
  "metric": true
}

'''

import sys
import json
import requests
import time

# get api and list of cities

def getKeyAndCities():

# first ensure that we know where the keys are kept !

  scriptpath = sys.path[0]
  keysrelpath = '../keys/astronomy.json'
  keypath = scriptpath + '/' + keysrelpath
  keypath = '/Users/pfs/Documents/keys/astronomy.json'

  f=open(keypath)
  j=f.read()
  f.close()
  astroCoords = json.loads(j)
  #print(astroCoords)

  return astroCoords


#using the city lat and lot to get both the sun and moon rises and sets

'''
https://weather.cit.api.here.com/weather/1.0/report.json?
product=forecast_astronomy\
&name=Geneva\
&app_id=DemoAppId01082013GAL\
&app_code=AJKnXv84fjrb0KIHawS0Tg\
'''

def currentRisesSets(astroCoords):

  myAppID = astroCoords['APP_ID']
  myAppCODE = astroCoords['APP_CODE']
  baseUrl = astroCoords['APP_URL']
  product = astroCoords['PRODUCT']
  myCity = astroCoords['City']
#  almanacDict = {}

  reqUrl = baseUrl + '?product=' + product + '&name=' + myCity + '&app_id=' + myAppID + '&app_code=' + myAppCODE

  r = requests.get(reqUrl)
  jData = r.json()
  print("")
  print(jData['astronomy']['astronomy'])
  print("")
  if r.ok :  
    almanacDictArray = jData['astronomy']['astronomy']
    # swap for region, instead of Lancy
    almanacDictArray[0]['city'] = jData['astronomy']['city']
  else:
    print('error from server', r.status_code)
    exit(1)
  return almanacDictArray

def printRisesSets(almanacDictArray):

  print(almanacDictArray[0]['city'])
  for almanacDict in almanacDictArray:
    print('Date: ', almanacDict['utcTime'], end = ' ')
    print('sun: ', almanacDict['sunrise'], almanacDict['sunset'], end = ' ')
    print('moon: ', almanacDict['moonrise'], almanacDict['moonset'], almanacDict['moonPhaseDesc'])
    print()
  return


def main():

  astroCoords = getKeyAndCities()
  almanacDict = currentRisesSets(astroCoords)
  printRisesSets(almanacDict)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()