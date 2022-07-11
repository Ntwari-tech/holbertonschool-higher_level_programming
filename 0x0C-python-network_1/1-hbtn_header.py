#!/usr/bin/python3
"""sends request to the url, displyas value of X-Request-Id"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv

    url = argv[1]
    r = request.Request(url)
    with request.urlopen(r) as response:
        print(response.headers.get('X-Request-Id'))
