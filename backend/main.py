from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI(title="Volleyball_Dashboard", version="1.0.0")