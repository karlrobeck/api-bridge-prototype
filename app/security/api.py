from typing import Annotated
from fastapi import APIRouter,HTTPException,status
from os import getenv
from .auth import create_token,decode_token,Header,get_hash,verify_hash,decode_b64,encode_b64
from .schemas import AuthAppRequestCredentials,AuthAppResponseCredentials,AuthCodeResponse,AuthRequestCode,AuthRequestCodePKCE,AuthTokenRequest,AuthTokenResponse

router:APIRouter = APIRouter(
    prefix='/v1/security',
    tags=['security'],
)

@router.post('/authorize')
def AuthorizeUser(user_req:AuthRequestCode) -> AuthCodeResponse:

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

    return AuthCodeResponse(
        code=code,
        state=user_req.state
    )

@router.post('/token')
def AuthorizeToken(user_req:AuthTokenRequest,encoded_data:Annotated[str,Header()]) -> AuthTokenResponse:

    grant_types = ['authorization_code']

    decoded_code = AuthRequestCode(**decode_token(user_req.code))

    if decode_b64(encoded_data).split(' ')[0] != 'Basic':
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail='invalid encoded_data format'
        )
    
    client_id,client_secret = decode_b64(encoded_data).split(' ')[1].split(':')

    if user_req.grant_type not in grant_types:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail='invalid grant_type'
        )
    
    print(user_req.redirect_uri,decoded_code)

    if user_req.redirect_uri != decoded_code.redirect_uri:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail='redirect uri doesnt match'
        )

    return AuthTokenResponse(
        access_token=create_token({'client_id':client_id,'client_secret':client_secret},True),
        token_type='bearer',
        scope=decoded_code.scope,
        expires_in=1111,
        refresh_token='test'
    )

@router.post('/app/register')
def AuthAppRegister(user_req:AuthAppRequestCredentials) -> AuthAppResponseCredentials:
    
    #register the app to database if not exist

    app_client_id:str = create_token(user_req.model_dump())

    app_client_secret:str = create_token({
        **user_req.model_dump(),
        'signature':get_hash(getenv('HASH_PASSWORD'))
    })
    
    return AuthAppResponseCredentials(
        client_id=app_client_id,
        client_secret=app_client_secret,
        client_credentials=encode_b64(f'Basic {app_client_id}:{app_client_secret}')
    )