from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import timedelta, datetime
from os import getenv
from base64 import b64decode,b64encode

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"/{getenv('API_VERSION')}/security/token")

def verify_hash(plain_str, hashed_str) -> bool:
    
    """
    Verify a hashed string against a plain string.

    Args:
        plain_str: The plain string.
        hashed_str: The hashed string.

    Returns:
        True if the hashes match, False otherwise.
    """

    return pwd_context.verify(plain_str, hashed_str)

def get_hash(plain_str:str) -> str:

    """
    Get the hash of a string.

    Args:
        string: The string to hash.

    Returns:
        The hash of the string.
    """

    return pwd_context.hash(plain_str)

def create_token(data: dict, expires_delta:bool=False) -> str:
    
    """
    Create a JSON Web Token (JWT).

    Args:
        data: The data to be encoded in the token.
        expires_delta: Whether or not the token should expire.

    Returns:
        The JWT.
    """

    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + timedelta(minutes=int(getenv('ACCESS_TOKEN_EXPIRE_MINUTES')))
        to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, getenv('API_SECRET_KEY'), algorithm=getenv('ALGORITHM'))
    return encoded_jwt

def decode_token(token:str) -> dict | None:
    
    """
    Decode a JSON Web Token (JWT).

    Args:
        token: The JWT to be decoded.

    Returns:
        The decoded JWT data, or None if the token is invalid.
    """
    
    return jwt.decode(token, getenv('API_SECRET_KEY'), algorithms=getenv('ALGORITHM'))

def generate_refresh_token():
    return 

def encode_b64(string:str) -> str:
    
    """
    Encode a string to base64.

    Args:
        string: The string to encode.

    Returns:
        The base64-encoded string.
    """
    
    return b64encode(string.encode('ascii')).decode('ascii')

def decode_b64(string:str) -> str:
    
    """
    Decode a base64-encoded string.

    Args:
        string: The base64-encoded string.

    Returns:
        The decoded string.
    """
    
    return b64decode(string.encode('ascii')).decode('ascii')

def verify_signature(token:str) -> bool | HTTPException:

    """
    Verify the signature of a JSON Web Token (JWT).

    Args:
        token: The JWT to be verified.

    Returns:
        True if the signature is valid, False otherwise.

    Raises:
        HTTPException: If the token is invalid.
    """

    try:
        decoded_token = decode_token(token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized Request"
        )
    
    if decoded_token['client_id']['name'] != decoded_token['client_secret']['name']:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized Request"
        )
    
    signature = decoded_token['client_secret']['signature']

    if not verify_hash(getenv('HASH_PASSWORD'),signature):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized Request"
        )
    
    return True

def verify_scope(token:str,func_scope:list | str | None) -> bool | HTTPException:

    """
    Verify the scope of a JWT token.

    Args:
        token: The JWT to be verified.
        scope: scope of the token. can be a list, string, or None

    Returns:
        True if the scope is valid, False otherwise.
        
    Raises:
        HTTPException: If the scope is invalid.

    """

    verify_signature(token)

    try:
        decoded_token = decode_token(token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized Request"
        )
    
    scopes:list = decoded_token['client_id']['scope'].split(' ')
    
    accepted:int = 0 

    for scope in func_scope:
        if scope.replace('_','-').lower() in scopes:
            accepted = accepted + 1

    if accepted != len(func_scope):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized Request"
        )
    
    return True