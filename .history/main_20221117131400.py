
import requests
import pprint
import json

url='https://jsonplaceholder.typicode.com/posts'
response=requests.get(url)
r=json.loads(response.text)



# url='https://jsonplaceholder.typicode.com/posts'
# response=requests.get(url)



# #pprint.pprint(response.json().get(url))
# pprint.pprint(response.json())
# resultado=response.json()
# first_ten=resultado[:10]
# #first_ten[:10]
