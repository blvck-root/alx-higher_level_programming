#!/bin/bash
# Send a POST request to passed URL, and display the response body
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
