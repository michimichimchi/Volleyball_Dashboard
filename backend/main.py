from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
#from schemas import
from db_engine import Base, engine, get_db, SessionLocal
from seed_db import seed_data
from models import User, Team, Match
import time
from sqlalchemy.exc import OperationalError

@asynccontextmanager
async def lifespan(app: FastAPI):
    # seed database
    # 5 tries to connect cause sometimes db container is not ready
    retries = 5
    while retries > 0:
        try:
            # create tables
            Base.metadata.create_all(bind=engine)
            # create database objects
            seed_data()
            print("succesfully seeded database", flush=True)
            break
        except OperationalError:
            print(f"database not ready, retry {retries} more times")
            retries -= 1
            time.sleep(3)
    yield

# create fastapi instance
app = FastAPI(title="Volleyball_Dashboard", version="1.0.0", lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}


