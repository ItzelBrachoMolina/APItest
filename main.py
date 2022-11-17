
import requests
import pprint
import json
from queue import Queue



url='https://jsonplaceholder.typicode.com/posts'
response=requests.get(url)



res=json.loads(response.text)
pprint.pprint(res[:10])
q=Queue(maxsize=10)
print('***************')

for r in res[:10]:
    q.put(r)

print("Full: ", q.full())


for r in res[:10]:
    q.get(r)

print('*/*******')


