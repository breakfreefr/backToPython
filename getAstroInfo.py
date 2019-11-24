#!python3

'''
Gets the sun and moon sunrise time from https://ipgeolocation.io/

nb: api key stored in ../keys/astroinfo.json and loaded when program run
along with the cities and the lat and long 

note : relative path !!! needs to find absolute directory of where the program is!

{
  "comment": "key info to get sun and moon rising and setting",
  "baseUrl": "https://api.ipgeolocation.io/astronomy",
  "apikey": APIKEY,
  "cities": [
    {"city": "York", "latitude": "53.9600", "longitude": "1.0873"},
    {"city": "Geneva", "latitude": "46.2044", "longitude": "6.1432"}
  ]
}

ie https://api.ipgeolocation.io/astronomy?apiKey=API_KEY&lat=-27.4748&long=153.017'

'''

import sys
import json

import requests
import time

# get api and list of cities

def getKeyAndCities():

# first ensure that we know where the keys are kept !

  scriptpath = sys.path[0]
  keysrelpath = '../keys/astroinfo.json'
  keypath = scriptpath + '/' + keysrelpath
  
  f=open(keypath)
  j=f.read()
  f.close()
  astroCoords = json.loads(j)
  apikey = astroCoords["apikey"]
  citiesList = astroCoords["cities"]
  return astroCoords


#using the city lat and lot to get both the sun and moon rises and sets

def currentRisesSets(astroCoords):

  myApiKey = astroCoords['apikey']
  baseUrl = astroCoords['baseUrl']
  almanacDict =[]

  for cityInfo in astroCoords['cities']:

    city = cityInfo['city']
    cLat = cityInfo['latitude']
    cLong = cityInfo['longitude']

    reqUrl = baseUrl + '?apiKey=' + myApiKey + '&lat=' + cLat + '&long=' + cLong
    r = requests.get(reqUrl)
    jData = r.json()
    if r.ok :  
      jData['city'] = city
      almanacDict.append(jData)
    else:
      print('error from server', r.status_code)
      exit(1)

  return almanacDict

def getRisesSets(almanacDict):

  for cityInfo in almanacDict:
    print(cityInfo['city'])
    print(cityInfo['sunrise'], cityInfo['sunset'] )
    print(cityInfo['moonrise'], cityInfo['moonset'])
    print()


def main():

  astroCoords = getKeyAndCities()
  almanacDict = currentRisesSets(astroCoords)
  getRisesSets(almanacDict)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()