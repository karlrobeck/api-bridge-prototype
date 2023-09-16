from os import getenv
from random import randint
from typing import Annotated
from fastapi import APIRouter,status,HTTPException
from .schemas import AppCredentials,AppInfo
from app.security.auth import get_hash,create_token
from database.db import checkRecord,insertRecord

app_register_router:APIRouter = APIRouter(
    prefix='/register'
)

@app_register_router.post(
    '/',
    status_code=status.HTTP_201_CREATED
)
def postAppRegister(user_req:AppInfo) -> AppCredentials:

    database_name:str = 'database/test.db'

    if checkRecord(database_name,'APP',[f"NAME = '{user_req.name}'"]):
        raise HTTPException(
            status_code=status.HTTP_302_FOUND
        )
    
    insertRecord(database_name,'APP',{'ID':randint(1,1000000000000),**user_req.model_dump()})

    return AppCredentials(
        client_id={**user_req.model_dump()},
        client_secret=create_token({
        **user_req.model_dump(),
        "signature":get_hash(getenv('HASH_PASSWORD'))})
    )

