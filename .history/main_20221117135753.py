
import requests
import pprint
import json
from queue import Queue

url='https://jsonplaceholder.typicode.com/posts'
response=requests.get(url)
res=json.loads(response.text)
pprint.pprint(res[:10])
print(type(res))
q=Queue(maxsize=10)

# for x,y in range(len(res[:10])):
#     print(res[x,y])
#     q.put(res[x,y])


print('***************')

print(q.full())



# import requests
# import pprint
# import json

# url='https://jsonplaceholder.typicode.com/posts'
# response=requests.get(url)
# r=json.loads(response.text)
# pprint.pprint(r[:10])
