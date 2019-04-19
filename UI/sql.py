import requests as req
import sys

text = input("enter url :")
file = open('data.txt', 'r')  # reading the data from file
payload = file.read().splitlines()
l = len(payload)

for x in range(l):  # attcking the address
    y = payload[x]
    resp = req.request(method='get', url=text, params=y)
    if resp.status_code == 200 and 300:
        print("found it Url: %s" % resp.url)
    else:
        print("trying man")