from pydantic import BaseModel

class AuthorizeBody(BaseModel):
    client_credentials:str
    response_type:str
    state:str
    scope:str

class ClientId(BaseModel):
    name:str
    app_type:str
    role:str
    scope:str

class ClientSecret(BaseModel):
    name:str
    signature:str

