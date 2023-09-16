from pydantic import BaseModel

class AppInfo(BaseModel):
    name:str
    description:str
    app_website:str
    redirect_uri:str
    app_type:str
    role:str
    scope:str

class AppCredentials(BaseModel):
    client_id:str
    client_secret:str