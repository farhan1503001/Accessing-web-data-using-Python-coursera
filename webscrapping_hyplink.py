import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
#Preparation for containing ssl errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
#url openern
url='http://py4e-data.dr-chuck.net/known_by_Leyland.html' #For person which Leyland knows
#url='http://py4e-data.dr-chuck.net/known_by_Fikret.html'
htm=urlopen(url,context=ctx).read()
#Initiating the beautiful soup object
soup=BeautifulSoup(htm,'html.parser')
#Finding all the links
def tag_finder(url1,pos,base_pos):
    temp_soup=BeautifulSoup(urlopen(url1,context=ctx).read(),'html.parser')
    temp_tags=temp_soup('a')
    temp_url=temp_tags[pos+base_pos].get('href',None)
    temp_name=temp_tags[pos+base_pos].contents[0]
    return temp_url,temp_name
tags=soup('a')
count=1
print(tags[0].contents[0])
base_pos=0
pos=17
url1=url
for i in range(7):
    url1,name=tag_finder(url1,pos,base_pos) 
    print(name)
