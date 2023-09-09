from pydantic import BaseModel

class AuthorizeBody(BaseModel):
    response_type:str=""
    state:str=""
    scope:str=""

class AuthorizationData(BaseModel):
    access_token:str=""
    refresh_token:str=""
    token_type:str=""
    scope:str=""


class ClientInfo(BaseModel):
    name:str=""
    app_type:str=""
    role:str=""
    scope:str=""

class ClientSecret(BaseModel):
    name:str=""
    signature:str=""

class Credentials(BaseModel):
    client_id:str=""
    client_secret:str=""
    client_credentials:str=""
    scopes:str=""