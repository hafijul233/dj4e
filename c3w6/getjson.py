# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The
# program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment
# counts from the JSON data, compute the sum of the numbers in the file and enter the sum below: We provide two files
# for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual
# data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553) Actual data:
# http://py4e-data.dr-chuck.net/comments_1018631.json (Sum ends with 67) You do not need to save these files to your
# folder since your program will read the data directly from the URL. Note: Each student will have a distinct data
# url for the assignment - so only use your own data url for analysis. Data Format The data consists of a number of
# names and comment counts in JSON as follows:
#
# { comments: [ { name: "Matthias" count: 97 }, { name: "Geomer" count: 97 } ... ] } The closest sample code that
# shows how to parse JSON and extract a list is json2.py. You might also want to look at geoxml.py to see how to
# prompt for a URL and retrieve data from a URL.

import json
import ssl
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Location: ')
jsonfile = urllib.request.urlopen(url, context=ctx).read()
print('Retrieving', url)
print('Retrieved ', len(jsonfile), ' characters')

# convert to xml tree
jsondict = json.loads(jsonfile)
allcomments = jsondict['comments']
# Retrieve all of the anchor tags
count = 0
total = 0
for comment in allcomments:
    count += 1
    total += int(comment['count'])

print('Count:', count)
print('Sum: ', total)
