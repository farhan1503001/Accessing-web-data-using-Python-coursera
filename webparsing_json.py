import json
import ssl
from urllib.request import urlopen
#Prompt asking for url
url=input("Enter location")
if len(url)<1:
    print("Enter url correctly")
#Handeling errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
#Now opening url and reading raw data and then decoding that
data=urlopen(url,context=ctx).read().decode()
#print(data) it's type is string now we will feed it json format
#Converting json format
js=json.loads(data)
#print(js)
infos=js['comments']
#Now accessing the names and counts
sum=0
for info in infos:
    #print(info['name'])
    sum=sum+int(info['count'])

print(sum)