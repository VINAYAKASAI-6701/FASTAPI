from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app=FastAPI()


class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    rating:Optional[int]=None

#creating data
my_posts=[{"title":"title if post 1","content":"content of post 1","id":1},{"title":"favourite foods","content":"i like pizza","id":2}]

@app.get("/")#we are hitting the api endpoint using get method
def root():
    return {"message":"Welcomem to my api!!!"}

def find_post(id):
    for p in my_posts:
        if p['id']==id:
            return p

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

#upating data
@app.post("/posts")
def create_posts(post:Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data":post_dict}
#we expect data that have title adn string,category of post,Boolean
#retreiving data
#lets creaet a dummy route


@app.get("/posts/{id}")
def get_post(id:int):
    print(id)
    post=find_post(id)
    print(post)
    return {"post_detail":post}


#lets creaet a dummy route
@app.get("/posts/latest")
def get_latest_post():
    post=my_posts[len(my_posts)-1]
    return {"detail":post}