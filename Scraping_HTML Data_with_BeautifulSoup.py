import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://py4e-data.dr-chuck.net/comments_1317326.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
sum = 0
count = 0
for tag in tags:
    sum = sum + int(tag.contents[0])
    count = count + 1
print('Count', count)
print('Sum', sum)
