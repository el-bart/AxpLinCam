#!/usr/bin/python
import sys
import requests

if len(sys.argv)==2:
    link=sys.argv[1]
else:
    link="https://www.baszerr.eu"

r = requests.get(link)

#print( r.text.encode("utf-8") )
#sys.exit(0)

print("response: " + str(r.status_code))
r.raise_for_status()
print("headers: " + str(r.headers))
print( "text: " + r.text.encode("utf-8") )
