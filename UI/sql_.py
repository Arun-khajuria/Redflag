import requests as req
import re
import sys

text = input("enter url")
file = open('C:\\project\\UI\\data.txt', 'r')
payload = (file.read())
l = len(payload)

for x in range(l):
    resp = req.request(method='get', url=text, params=payload)
    print(resp.status_code)
