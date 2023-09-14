from pydantic import BaseModel

class AuthRequestCode(BaseModel):
    client_id:str=""
    response_type:str=""
    redirect_uri:str=""
    state:str=""
    show_dialog:bool=False
    scope:str=""

class AuthRequestCodePKCE(AuthRequestCode):
    code_challenge_method:str=""
    code_challenge:str=""

class AuthCodeResponse(BaseModel):
    code:str=""
    error:str=""
    state:str=""

class AuthTokenRequest(BaseModel):
    code:str=""
    redirect_uri:str=""
    grant_type:str=""

class AuthTokenResponse(BaseModel):
    access_token:str
    token_type:str
    scope:str
    expires_in:int
    refresh_token:str

class AuthAppRequestCredentials(BaseModel):
    name:str
    app_type:str
    role:str

class AuthAppResponseCredentials(BaseModel):
    client_id:str
    client_secret:str
    client_credentials:str
