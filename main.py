# Imports
from fastapi import FastAPI
import uvicorn

# Create a FastAPI instance
app = FastAPI()

# Define the /hello endpoint
@app.get("/hello")
def hello():
    return "Bye"

# Run the application when the script is executed directly
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=1000, reload=True)