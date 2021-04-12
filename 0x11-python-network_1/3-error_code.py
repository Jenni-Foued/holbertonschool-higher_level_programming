#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
and displays the body of the response decoded in utf-8
"""
if __name__ == "__main__":
    import urllib.request
    from sys import argv
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
