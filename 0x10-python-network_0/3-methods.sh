#!/bin/bash
# Bash script that takes in an URL and displays all HTTP methods the server will accept
curl -sIX OPTIONS "$1" | grep "Allow:" | cut -c8-
