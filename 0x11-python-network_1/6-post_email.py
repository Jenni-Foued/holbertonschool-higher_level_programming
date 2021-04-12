#!/usr/bin/python3
"""
takes in a URL and an email address
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    Data = {'email': argv[2]}
    url = argv[1]
    r = requests.post(url, data=Data)
    print(r.text)
