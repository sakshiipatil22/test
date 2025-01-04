from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hello")
def hello():
    return "Bye"
    
data = {
    "Sakshi": {
        "name": "Sakshi",
        "number": "8917273212",
        "dob": "22/02/2004"
    },
    "Rahul": {
        "name": "Rahul",
        "number": "9087221322",
        "dob": "10/05/2005"
    },
    "Sejal": {
        "name": "Sejal",
        "number": "8989775754",
        "dob": "21/04/2000"
    },
    "Aditya": {
        "name": "Aditya",
        "number": "9088743212",
        "dob": "10/11/1998"
    }
}

@app.get("/get-name")
def get_name(name:str):
    response = data.get(name.capitalize(), {"Error": "Name not found"})
    return response
    

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=1000, reload=True)