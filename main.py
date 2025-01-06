from fastapi import FastAPI, HTTPException
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
    try:
        for person in data:
            if person.get("name", "").lower() == name.lower():
                return {
                    "name": person.get("name", "Unknown"),
                    "address": person.get("address", "Not Provided"),
                    "dob": person.get("dob", "Not Provided"),
                    "number": person.get("number", "Not Available"),
                }
        raise HTTPException(status_code=404, detail="Name not found")
    except HTTPException as e:
        raise e
    except Exception as e:
        return {"error": "An unexpected error occurred", "details": f"Name not found:{e}"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8085, reload=True)