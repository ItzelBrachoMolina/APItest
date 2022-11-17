
import requests
import pprint

url='https://jsonplaceholder.typicode.com/posts'
response=requests.get(url)



#pprint.pprint(response.json().get(url))
#pprint.pprint(response.json())
first_ten=response.json()
first_ten[:10]
