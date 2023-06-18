import json, requests

url = 'https://api.spacetraders.io/v2/'

x = requests.get(url)
print(x.text)

###
# POST requests
# requests.post(url, json = obj)
#   where obj is the data
# timeout = wait until stop, otherwise will wait until
#   connection is closed
###