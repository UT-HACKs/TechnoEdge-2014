#!/usr/bin/env bash
 
username=@ly9988
password=rugiya
locations=139.694123,35.683192,139.709272,35.694555 
url=https://stream.twitter.com/1/statuses/filter.json
while :
do
  curl -d locations=139.694123,35.683192,139.709272,35.694555 -m 240 -u @ly9988:rugiya https://stream.twitter.com/1/statuses/filter.json
done