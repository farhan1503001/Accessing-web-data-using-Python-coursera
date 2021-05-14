import json
import ssl
from urllib.request import urlopen,urlretrieve
import urllib.parse
#As for this experiment we have no api key of our own
api_key=False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
#Prompt for location input
location=input("Enter location")
if len(location)<0:
    print("Operation cannot be performed.Insert correct place")
else:
    parameters=dict()
    parameters['address']=location
    if api_key is not False:
        parameters['key']=api_key

    #Now creating url
    url=serviceurl+urllib.parse.urlencode(parameters)
    #Now reading from the url
    data=urlopen(url,context=ctx).read().decode()
    try:
        js=json.loads(data)
    except:
        js=None
    if not js or js['status']!='OK' or 'status' not in js:
        print("Failure to Retrive---------------------")
        print(data)
    else:
        print(js['results'][0]['place_id'])
