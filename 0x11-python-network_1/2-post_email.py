#!/usr/bin/python3
"""
Takes in a URL and an email, sends a request to the URL with the email as param
and displays the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    import urllib.request
    from sys import argv
    import urllib.parse
    data = urllib.parse.urlencode({'email': argv[2]})
    data = data.encode('ascii')
    with urllib.request.urlopen(argv[1], data) as response:
        print(response.read().decode('utf-8'))
