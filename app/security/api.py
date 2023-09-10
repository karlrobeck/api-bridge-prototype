from typing import Annotated
from fastapi import APIRouter,status, Header,HTTPException
from os import getenv
from .auth import create_token,decode_token,encode_b64,decode_b64,verify_hash,get_hash
from .types import AuthorizeBody,ClientInfo,ClientSecret,Credentials,AuthorizationData

router:APIRouter = APIRouter(prefix=f"/{getenv('API_VERSION')}/security")    

@router.post('/authorize')
async def authorizeToken(req:AuthorizeBody,client_credentials:str=Header()) -> AuthorizationData | HTTPException:
    """
    Authorizes a client with the given client credentials.

    Args:
        req: The request body.
        client_credentials: The client credentials header.

    Returns:
        The authorization data.

    Raises:
        HTTPException: If the request is invalid.
    """

    if req.response_type != 'json':
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="response_type must be equal to json"
        )

    # Decode the client header.
    try:
        decoded_header = decode_b64(client_credentials)
    except:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Invalid Authorization Header"
        )

    if len(decoded_header.split(' ')) != 2:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid client credentials format"
        )

    # Check if the client credentials are in the correct format.
    if decoded_header.split(' ')[0] != 'Authorization':
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid client credential format"
        )

    # Get the client header.
    client_header = decoded_header.split(' ')[1].split(':')

    # Decode the client_id.
    decoded_client_id = decode_token(client_header[0])
    
    # Decode the client_id.
    decoded_client_secret = decode_token(client_header[1])

    # Check if the client_id and client_secret belong to each other.
    if decoded_client_id['name'] != decoded_client_secret['name']:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="client id and client secret not match"
        )
    
    # Verify if the client secret is signed by the system.
    if not verify_hash(getenv('HASH_PASSWORD'),decoded_client_secret['signature']):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unautorized Request"
        )

    # Return a new access token.
    return AuthorizationData(
        access_token=create_token({
            "client_id":decoded_client_id,
            "client_secret":decoded_client_secret,
            "scope":req.scope
        },expires_delta=True),
        refresh_token=create_token({
            "client_id":decoded_client_id,
            "client_secret":decoded_client_secret,
            "scope":req.scope,
            "refresh_hash":get_hash(getenv('REFRESH_TOKEN_KEYWORD'))
        }),
        scope=req.scope,
        token_type="bearer"
    )

@router.post('/register')
async def register(request:ClientInfo,gateway_password:Annotated[str,Header()]) -> Credentials | HTTPException:
    """
    Registers a new client.

    Args:
        request: The client information.
        gateway_password: The gateway password.

    Returns:
        The credentials for the new client.

    Raises:
        HTTPException: If the request is invalid or the gateway password is incorrect.
    """

    if getenv('GATEWAY_SECRET_KEY') != gateway_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unautorized Request"
        )
    
    # Create a client ID and client secret.
    client_id = create_token(request.model_dump())
    client_secret = create_token(ClientSecret(
        name=request.name,
        signature=get_hash(getenv('HASH_PASSWORD'))
    ).model_dump())

    # Return the credentials for the new client.
    return Credentials(
        client_id=client_id,
        client_secret=client_secret,
        client_credentials=encode_b64(f'Authorization {client_id}:{client_secret}'),
        scopes=request.scope
    )
    

