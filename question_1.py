import requests
import json
# post api use here.
url = "https://my-json-server.typicode.com/typicode/demo/posts"

data={}

r= requests.get(url=url,data=data)
data = r.json()
post = data


# comment api use here.
url1 = "https://my-json-server.typicode.com/typicode/demo/comments"

data={}

r= requests.get(url=url1,data=data)
data = r.json()
comment=data


def post_comment(post,comment):
	d=len(post)

	for x,q in zip(post,range(d)):
		li=[]
		for y in comment:
			if x["id"] == y["postId"]:
				li.append(y)		
			
		post[q]["comments"]=li
	return post
	
print(post_comment(post,comment))