#!/usr/bin/python3
"""fetches URL using requests"""
if __name__ == '__main__':
    import requests

    r = requests.get('https://intranet.hbtn.io/status')
    print(f"Body response:\n\t- type: {type(r.text)}\n\t- content: {r.text}")
