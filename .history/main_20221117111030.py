
import requests
import pprint

url='https://jsonplaceholder.typicode.com/posts'
args=10
response=requests.get(url,params=args)

pprint.pprint(response.json().get('userId'))