import json, requests

url = 'https://api.spacetraders.io/v2/'

x = requests.get(url)
# print(x.text)

jsonParsed = json.loads(x.text)
print(jsonParsed["status"])

for key in jsonParsed:
    print(key +":", jsonParsed[key])

###
# POST requests
# requests.post(url, json = obj)
#   where obj is the data
# timeout = wait until stop, otherwise will wait until
#   connection is closed
###

