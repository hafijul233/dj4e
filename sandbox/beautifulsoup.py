from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

span_count = 0
span_total = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    span_total += int(tag.text)
    span_count+=1

print("Total:", span_total,"Count:", span_count)
