import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    #Reading the url data using urllib
    data = urllib.request.urlopen(url, context=ctx).read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())#Converting data from byte array to string using decode
    tree = ET.fromstring(data)

    results = tree.findall('result/geometry/location')
    lat = results[0].find('lat').text
    lng = results[0].find('lng').text
    #location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    result_address=tree.findall('result')
    location=result_address[0].find('formatted_address').text
    print(location)