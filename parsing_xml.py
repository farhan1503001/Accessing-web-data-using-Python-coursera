import xml.etree.ElementTree as et
import ssl
from urllib.request import urlopen
#SSL certification error handeling
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
#Reading url using urlib
#url='http://py4e-data.dr-chuck.net/comments_42.xml'
url='http://py4e-data.dr-chuck.net/comments_1243935.xml'
htm=urlopen(url,context=ctx).read()
xml_string=htm.decode()#Converting byte array htm to string
#print(xml_string[0])
#Now building the parse tree from the string
xml_data=et.fromstring(xml_string)
#Now we will find the branch of the xml tree 
results=xml_data.findall('comments/comment')
sum=0
for result in results:
    sum=sum+int(result.find('count').text)
print(sum)
    