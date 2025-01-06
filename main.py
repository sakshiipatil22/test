from fastapi import FastAPI
import uvicorn

app = FastAPI()

data = [
    {
        "name": "Sakshi",
        "address": "xkbfdkn",
        "dob": "22/02/2004",
        "number": "8917273212",
    },
    {
        "name": "Rahul",
        "address": "xkbfdkn",
        "dob": "10/05/2005",
        "number": "9087221322",
    },
    {
        "name": "Sejal",
        "address": "xkbfdkn",
        "dob": "21/04/2000",
        "number": "8989775754",
    },
    {
        "name": "Aditya",
        "address": "xkbfdkn",
        "dob": "10/11/1998",
        "number": "9088743212",
    },
]

@app.get("/hello")
def hello():
    return "Bye"

@app.get("/get-name")
def get_name(name: str):
    for person in data:
        if person["name"].lower() == name.lower():
            return person
    return {"error": "Name not found"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=1000, reload=True)