from fastapi import FastAPI
from routes.astrology import router


app = FastAPI()

# Register routes
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Astrology API"}
