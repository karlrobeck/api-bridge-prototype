from pydantic import BaseModel

class SecurityRequestCode(BaseModel):
    client_id:str=""
    response_type:str=""
    redirect_uri:str=""
    state:str=""
    show_dialog:bool=False
    scope:str=""

class SecurityRequestCodePKCE(SecurityRequestCode):
    code_challenge_method:str=""
    code_challenge:str=""

class SecurityCodeResponse(BaseModel):
    code:str=""
    error:str=""
    state:str=""

class SecurityTokenRequest(BaseModel):
    code:str=""
    redirect_uri:str=""
    grant_type:str=""

class SecurityTokenResponse(BaseModel):
    access_token:str
    token_type:str
    scope:str
    expires_in:int
    refresh_token:str

class SecurityRequestCredentials(BaseModel):
    name:str
    description:str
    app_website:str
    redirect_uri:str
    app_type:str
    role:str
    scope:str

class SecurityResponseCredentials(BaseModel):
    client_id:str
    client_secret:str
    client_credentials:str
