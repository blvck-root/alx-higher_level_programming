#!/bin/bash
# Send JSON POST request to URL and display the response body
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
