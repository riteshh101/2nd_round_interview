import requests

import json



def user_lst():
	user_count=0
	for x in range(1,13):
		url = "https://reqres.in/api/users?page="+str(x)
		data={}
		r= requests.get(url=url,data=data)
		data=r.json()
		user_count = user_count +len(data["data"])
	return user_count	
print("Total number of user=",user_lst())
		