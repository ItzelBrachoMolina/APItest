
import requests
import pprint
import json
from queue import Queue


#client_id=c6ec3913de5daafb0926
#client_secret=7a88556c9488d1864ff8dca71dba05c09ffa8855

url='https://jsonplaceholder.typicode.com/posts'
response=requests.get(url)
res=json.loads(response.text)
pprint.pprint(res[:10])
q=Queue(maxsize=10)
print('***************')

for r in res[:10]:
    #print(r)
    q.put(r)

print("Full: ", q.full())


for r in res[:10]:
    #print(r)
    q.get(r)

print('*/*******')



filtered_results=[]

for index in range(len(results)):
    for key in results[index]:
        if results[index][key] > 5:
            filtered_results.append(key)

print(filtered_results)