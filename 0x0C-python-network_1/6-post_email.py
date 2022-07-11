#!/usr/bin/python3
"""sends POST to URL and displays response"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
