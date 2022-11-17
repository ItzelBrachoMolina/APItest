
import requests
import pprint

url='https://jsonplaceholder.typicode.com/posts'
response=requests.get(url)



#pprint.pprint(response.json().get(url))
pprint.pprint(response.json())
resultado=response.json()
first_ten=resultado[:10]
#first_ten[:10]
