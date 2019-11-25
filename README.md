# backToPython
bits of simple test code stored on breakfreefr@github.com

**minijib**

first off is the four words - modified to five letter words used to generate a random string for mild passwords.

*note* no filtering on words in the dictionary, ie unsanitized !!! beware.

**lcdWords**

for the writing to the lcd module, we first need to get the following module

<script src="https://gist.github.com/vay3t/8b0577acfdb27a78101ed16dd78ecba1.js"></script>

will write new set of phrases to the lcd module every second, scrolling down.

**getWeather**

use open weather (https://openweathermap.org/) and an api key to get weather for cities listed in the ../key directory, check 

```
{
  "key": "xxxxxxxxxxxxxxxxxxxx",
  "cities": {
    "York": "2633352",
    "Geneva": "6458784"
  }
}
```

nb: for city id consonsult : https://openweathermap.org/current#cityid

**getAstroInfo**

uses https://ipgeolocation.io and api key to get sunrise, sunset, moonrise, moonset for listed cities in a json key file:

```
{
  "comment": "key info to get sun and moon rising and setting",
  "baseUrl": "https://api.ipgeolocation.io/astronomy",
  "apikey": APIKEY,
  "cities": [
    {"city": "York", "latitude": "53.9600", "longitude": "1.0873"},
    {"city": "Geneva", "latitude": "46.2044", "longitude": "6.1432"}
  ]
}
```
