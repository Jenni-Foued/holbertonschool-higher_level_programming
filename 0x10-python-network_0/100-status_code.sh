#!/bin/bash
# Bash script that sends a request to an URL passed as an argument and displays only the status code of the response
curl -so /dev/null -w "%{http_code}" "$1"
