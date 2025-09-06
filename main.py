from fastapi import FastAPI

app=FastAPI()

@app.get("/")#we are hitting the api endpoint using get method
def root():
    return {"message":"Welcomem to my api!!!"}

@app.get("/posts")
def get_posts():
    return {"data":"This is my data"}