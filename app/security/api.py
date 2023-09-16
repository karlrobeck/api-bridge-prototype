import random
from typing import Annotated
from fastapi import APIRouter,HTTPException,status,Header
from fastapi.responses import RedirectResponse
from database.db import checkRecord,getRecord,updateRecord,insertRecord,tableSize
from os import getenv
from .auth import (
    create_token,
    decode_b64,
    decode_token,
    get_hash,
    verify_hash,
    encode_b64
)
from .schemas import (
    SecurityRequestCodePKCE,
    SecurityCodeResponse,
    SecurityRequestCode,
    SecurityRequestCredentials,
    SecurityResponseCredentials,
    SecurityTokenRequest,
    SecurityTokenResponse
)

router:APIRouter = APIRouter(
    prefix='/v1/security',
    tags=['security'],
)

@router.post('/authorize')
def AuthorizeUser(user_req:SecurityRequestCode) -> SecurityCodeResponse:

    # check if client id is correct format and in database
    try:
        client_id = decode_token(user_req.client_id)
    except:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail='invalid client id'
        )
    
    if user_req.response_type != 'code':
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail='response type must be code'
        )

    if user_req.redirect_uri == '':
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail='invalid redirect_uri'
        )
    
    code = create_token(user_req.model_dump())

    return SecurityCodeResponse(
        code=code,
        error="",
        state=user_req.state
    )

@router.post('/token')
def AuthorizeToken(user_req:SecurityTokenRequest,encoded_data:Annotated[str,Header()]) -> SecurityTokenResponse:

    grant_types = ['authorization_code']

    decoded_code = SecurityRequestCode(**decode_token(user_req.code))

    if encoded_data.split(' ')[0] != 'Basic':
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail='invalid encoded_data format'
        )
    
    client_id,client_secret = decode_b64(encoded_data.split(' ')[1]).split(':')

    if user_req.grant_type not in grant_types:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail='invalid grant_type'
        )

    if user_req.redirect_uri != decoded_code.redirect_uri:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail='redirect uri doesnt match'
        )

    return SecurityTokenResponse(
        access_token=create_token({'client_id':client_id,'client_secret':client_secret},True),
        token_type='bearer',
        scope=decoded_code.scope,
        expires_in=1111,
        refresh_token='test'
    )

@router.post('/app/register')
def postAuthAppRegister(user_req:SecurityRequestCredentials) -> SecurityResponseCredentials:
    
    #register the app to database if not exist
    database_name = 'database/test.db'

    if checkRecord(database_name,'APP',[f"NAME = '{user_req.name}'"]):
        raise HTTPException(
            status_code=status.HTTP_302_FOUND
        )
    
    print('does not exist')
    insertRecord(database_name,'APP',{'ID':random.randint(1,1000000000000),**user_req.model_dump()})
    print('data added to server')

    app_client_id:str = create_token(user_req.model_dump())

    app_client_secret:str = create_token({
        **user_req.model_dump(),
        'signature':get_hash(getenv('HASH_PASSWORD'))
    })
    
    return SecurityResponseCredentials(
        client_id=app_client_id,
        client_secret=app_client_secret,
        client_credentials=f"Basic {encode_b64(f'{app_client_id}:{app_client_secret}')}"
    )
    