from fastapi import FastAPI
from routes import astrology
from databases import Database

app = FastAPI()

# Register routes
app.include_router(astrology.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Astrology API"}

DATABASE_URL = "postgresql://postgres:password@postgres:5432/astrology_db"

database = Database(DATABASE_URL)
# To be used in FastAPI routes
async def connect_to_db():
    await database.connect()

async def disconnect_from_db():
    await database.disconnect()