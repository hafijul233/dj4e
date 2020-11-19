import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://hafijulislam.adovasoft.com')

for line in fhand:
    print(line.decode().strip())
