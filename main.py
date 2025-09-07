from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app=FastAPI()


class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    rating:Optional[int]=None


@app.get("/")#we are hitting the api endpoint using get method
def root():
    return {"message":"Welcomem to my api!!!"}

@app.get("/posts")
def get_posts():
    return {"data":"This is my data"}

@app.post("/createposts")
def create_posts(new_post:Post):
    print(new_post)
    print(new_post.dict())
    return {"data":new_post}
#we expect data that have title adn string,category of post,Boolean

