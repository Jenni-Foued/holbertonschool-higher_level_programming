#!/bin/bash
# Bash script that takes in an URL as an argument, sends a GET request to the URL and displays the body of the response
curl "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
