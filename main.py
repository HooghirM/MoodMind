#MoodMind app entry point 
#FastAPI will be used here


# Importing FastAPI class from FastAPI library
from fastapi import FastAPI

# Importing router object created inside app/routers/health.py
from app.routers.health import router

# Creating instance of FastAPI class
app = FastAPI()

# A decorator that defines the route
@app.get("/")
# Defines asynchronous function named root
async def root():
    # Return value is a Json response... just a placeholder response.
    return {"message": "Hello World"}

# Attaches router to main FastAPI App/ appliex V1 prefix.
app.include_router(router, prefix="/v1")
