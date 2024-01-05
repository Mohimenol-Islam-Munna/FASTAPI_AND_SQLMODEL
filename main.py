from fastapi import FastAPI

# create  fastapi instance 
app = FastAPI(debug=True)

@app.get("/")
def home():
    return "This is home route of our application"