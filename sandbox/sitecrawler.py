from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

ahref = ['Parker']

for i in range(1,8):
	html = urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, "html.parser")
	# Retrieve all of the anchor tags
	tags = soup('a')
	count = 0
	for tag in tags:
		count +=1
		if count == 18:
			url = tag.get('href', '#')
			ahref.append(tag.text)
			break

for name in ahref:
        print(name)
