# Lecture 4: (Libraries/API)
# JSON - is a text file that is used to exchange data between appliccations.
import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))