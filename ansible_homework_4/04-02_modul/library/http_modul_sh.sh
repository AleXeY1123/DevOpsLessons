#!/bin/bash
# WANT_JSON

uri=$(cat $1 | grep -Po '(?<="adress": ")(.*?)(?=")')

result_string=$(curl -o /dev/null --silent --head --write-out '%{http_code}\n' $uri)

echo "{\"result_str\": \"$result_string\", \"msg\": \"Success\"}"
