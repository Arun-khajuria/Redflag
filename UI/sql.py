import requests as req
import sys
import time

text = input("enter url : ")
file = open('data.txt', 'r')  # reading the data from file
payload = file.read().splitlines()
l = len(payload)

for x in range(l):  # attcking the address
    y = payload[x]
    resp = req.request(method='get', url=text, params=y)

    if resp.status_code == 200 and 300:
        print("found it Url: %s " % (resp.url))

    elif resp.status_code == 400:
        print("you Might check %s %s" % (resp.url, resp.headers))
        exit()
    else:
        print("trying man")