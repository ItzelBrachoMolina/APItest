
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

for r in res:
    print(r)
    q.put(r)

print(q.queue) 


print('***************')

print(q.full())



# import requests
# import pprint
# import json

# url='https://jsonplaceholder.typicode.com/posts'
# response=requests.get(url)
# r=json.loads(response.text)
# pprint.pprint(r[:10])
