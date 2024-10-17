import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
response = requests.get("http://itune.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())

# using json lib
o = response.json()
for result in o["result"]:
    print(result["trackName"])