# Imports
from fastapi import FastAPI
import uvicorn

/*# Create a FastAPI instance
app = FastAPI()

# Define the /get-name endpoint
@app.get("/get-name")
def get_name(name: str):
    # Predefined name and number mapping
    data = {
        "sakshi": {"name": "Sakshi", "number": "9637271127"},
        "rahul": {"name": "Rahul", "number": "7890123456"},
        "ananya": {"name": "Ananya", "number": "9876543210"},
        "arjun": {"name": "Arjun", "number": "4567891230"},
    }

    # Get response for the requested name
    response = data.get(name.lower(), {"error": "Name not found"})  # Default if name doesn't exist
    return response

# Run the application when the script is executed directly
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=1000, reload=True)
