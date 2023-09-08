from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import timedelta, datetime
from os import getenv
from .types import ClientId,ClientSecret
from base64 import b64decode,b64encode

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"/{getenv('API_VERSION')}/security/token")

def verify_hash(plain_str, hashed_str):
    return pwd_context.verify(plain_str, hashed_str)

def get_hash(string:str) -> str:
    return pwd_context.hash(string)

def create_token(data: dict, expires_delta:bool=False) -> str:
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + timedelta(minutes=int(getenv('ACCESS_TOKEN_EXPIRE_MINUTES')))
        to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, getenv('API_SECRET_KEY'), algorithm=getenv('ALGORITHM'))
    return encoded_jwt

def decode_token(token:str) -> dict | None:
    return jwt.decode(token, getenv('API_SECRET_KEY'), algorithms=getenv('ALGORITHM'))

def generate_refresh_token():
    return 

def decode_client_secret(client_secret:str):
    return decode_token(client_secret)

def encode_b64(string:str):
    return b64encode(string.encode('ascii')).decode('ascii')

def decode_b64(string:str):
    return b64decode(string.encode('ascii')).decode('ascii')