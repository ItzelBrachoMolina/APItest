
import requests
import pprint
import json
from queue import Queue

url='https://jsonplaceholder.typicode.com/posts'
response=requests.get(url)
r=json.loads(response.text)
pprint.pprint(r[:10])





# import requests
# import pprint
# import json

# url='https://jsonplaceholder.typicode.com/posts'
# response=requests.get(url)
# r=json.loads(response.text)
# pprint.pprint(r[:10])
