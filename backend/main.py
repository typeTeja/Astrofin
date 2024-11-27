from fastapi import FastAPI
from routes import astrology

app = FastAPI()

# Register routes
app.include_router(astrology.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Astrology API"}
