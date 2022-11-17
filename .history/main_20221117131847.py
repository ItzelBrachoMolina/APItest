
import requests
import pprint
import json

url='https://jsonplaceholder.typicode.com/posts'
response=requests.get(url)
r=json.loads(response.text)
r.sort()
pprint.pprint(r[:10])


