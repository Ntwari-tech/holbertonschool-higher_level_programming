#!/usr/bin/python3
from re import U
import urllib.request
""" website fetcher """
with urllib.request.urlopen('https://intranet.hbtn.io/status/') as r:
    html = r.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))


#!/usr/bin/python3
import urllib.request
"""this code is a web fetcher"""
html = r.read()
print("body response:")
print("\t- type: {}".format(type(html)))
print("\t- content: {}".format(html))
print("\t- utf8 content: {}".format(html.decod('utf-8')))
