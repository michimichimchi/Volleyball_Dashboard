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
import traceback

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
        except Exception as e:
            print("=== Kbackend error ===", flush=True)
            traceback.print_exc()
            break
    yield

# create fastapi instance
app = FastAPI(title="Volleyball_Dashboard", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def healthcheck():
    return {"status": "healthy"}