from typing import Annotated
from fastapi import APIRouter,status,HTTPException
from .schemas import AppInfo
from database.db import checkRecord,getRecord

application_info_router:APIRouter = APIRouter(
    prefix='/info'
)

@application_info_router.get(
    '/',
    status_code=status.HTTP_200_OK
)
def getApplicationInfo() -> dict:

    database_name = 'database/test.db'

    if not checkRecord(database_name,'APP',[f"NAME = 'sample app'"]):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    return {"data":getRecord(database_name,'APP',condition=[f"NAME = 'sample app'"])}

@application_info_router.post(
    '/',
    status_code=status.HTTP_201_CREATED
)
def postApplicationInfo() -> AppInfo:
    return AppInfo()

@application_info_router.put(
    '/',
    status_code=status.HTTP_205_RESET_CONTENT
)
def putApplicationInfo() -> AppInfo:
    return AppInfo()

@application_info_router.delete(
    '/',
    status_code=status.HTTP_204_NO_CONTENT
)
def deleteApplicationInfo():
    return AppInfo()
