#!/bin/bash
# Take in a URL, send request, and display size of the response body
curl -sI "$1" | awk '/Content-Length/{print $2}'
