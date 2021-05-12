import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
#Preparing context for handeling SSL certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
#Opening the url
url=urlopen('http://py4e-data.dr-chuck.net/comments_1243933.html',context=ctx) #http://py4e-data.dr-chuck.net/comments_42.htm
htm=url.read()
#Printing the data in html format
#print(htm)
#Now using Beautiful soap to parse html data
soup=BeautifulSoup(htm,'html.parser')
#print(soup)
#Now search for number
spans=soup('span')
#print(spans)
sum=0
for span in spans:
    #print(span.contents[0])#Finding the contents of the span class
    sum=sum+int(span.contents[0])
print(sum)


