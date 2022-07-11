#!/usr/bin/python3
"""sends request to URL and displays response with HTTPError handling"""
if __name__ == "__main__":
    import urllib.request as request
    import urllib3 as error
    import sys

    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(str(response.read(), 'utf-8'))
    except error as e:
        print("Error code: {}".format(e.code))
