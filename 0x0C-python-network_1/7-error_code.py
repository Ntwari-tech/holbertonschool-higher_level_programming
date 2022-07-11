#!/usr/bin/python3
"""requests from URL with error handling"""
if __name__ == "__main__":
    import requests
    import sys
    r = requests.get(sys.argv[1])
    if r.status_code <= 400:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
