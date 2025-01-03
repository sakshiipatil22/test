
from fastapi import FastAPI
import uvicorn


app = FastAPI()

# Define the /get-name endpoint
@app.get("/get-name")
def get_name(name: str):
    
    data = {
        "sakshi": {"name": "Sakshi", "number": "9637271127"},
        "rahul": {"name": "Rahul", "number": "7890123456"},
        "ananya": {"name": "Ananya", "number": "9876543210"},
        "arjun": {"name": "Arjun", "number": "4567891230"},
    }

    
    response = data.get(name.lower(), {"error": "Name not found"})  
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=1000, reload=True)
