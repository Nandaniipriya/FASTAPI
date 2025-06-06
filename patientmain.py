from fastapi import FastAPI
import json

# single endpoint
app= FastAPI()

# to return the json files data this function is used
def load_data():
    with open('patients.json', 'r') as f:
        data=json.load(f)
    return data
        
@app.get("/")## this is an object
def hello():
    return {"message": "Patient management system API"}
## to run this code we take the help of uvicorn.
@app.get("/about")
def about():
    return {"message": "A fully functional API TO MANAGE YOUR PATIENTS RECORDS"}
@app.get("/view")
def view():
    data=load_data()
    return data