#!/bin/bash
# Display status code of the response from a URL request
curl -sw "%{http_code}" "$1" -o /dev/null
