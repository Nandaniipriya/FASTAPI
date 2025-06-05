from fastapi import FastAPI
# single endpoint
app= FastAPI()

@app.get("/")## this is an object
def hello():
    return {"message": "Hello, World!"}
## to run this code we take the help of uvicorn.
@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application."}