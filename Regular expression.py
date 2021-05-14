import re
import urllib.request,urllib
import ssl
#Preparing ssl certificates
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
#Reading the data from web
url='http://py4e-data.dr-chuck.net/regex_sum_42.txt'
data=urllib.request.urlopen(url,context=ctx).read().decode()
#print(data)
numbers=re.findall('[0-9]+',data)
sum=0
print(len(numbers))
for num in numbers:
    sum=sum+int(num)
print(sum)
