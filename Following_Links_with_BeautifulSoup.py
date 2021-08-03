import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://py4e-data.dr-chuck.net/known_by_Brigitte.html'
print(url)
count = int(input('Enter count'))
pos = int(input('Enter Position'))
while True:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    ct = 0
    print('Retrieving: ', url)
    for tag in tags:
        ct = ct + 1
        if ct == pos:
            url = tag.get('href', None)
            break
    count = count - 1
    if count == 0:
        break
print('Retrieving: ', url)
