#!/usr/bin/python3
"""sends request to URL and displays the X-Request-Id"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
