from ..main import app
from fastapi import status
from fastapi.testclient import TestClient
from ..security.types import ClientInfo,AuthorizeBody,Credentials,AuthorizationData
from ..routes.onesti.types import StudentGrades
from os import getenv

route = f"/{getenv('API_VERSION')}/onesti"

client = TestClient(app)


def test_grades_routes():
    
    #Authorization 
    register_response = Credentials(**client.post(
        f'v1/security/register',
        headers={"gateway-password":getenv('GATEWAY_SECRET_KEY')},
        json=ClientInfo(
            name="Test Client",
            app_type="basic",
            role="basic",
            scope="user-read-grades user-update-grades user-create-grades user-delete-grades"
        ).model_dump()
    ).json())

    authorize_response = AuthorizationData(**client.post(
        f'v1/security/authorize',
        headers={'client-credentials':register_response.client_credentials},
        json=AuthorizeBody(
            response_type='json',
            state='cfea1cb0f712301802c072edb35a912a5a2af20a06fb86884c829af3923c4bc4',
            scope=register_response.scopes
        ).model_dump()
    ).json())

    #Route testing
    assert client.get(
        f'{route}/grades',
        headers={'access-token':authorize_response.access_token}
    ).status_code == status.HTTP_200_OK

    assert list(client.get(
        f'{route}/grades',
        headers={'access-token':authorize_response.access_token}
    ).json().keys()) == list(StudentGrades().model_dump().keys())
    
    assert client.post(
        f'{route}/grades',
        headers={'access-token':authorize_response.access_token}
    ).status_code == status.HTTP_201_CREATED

    assert list(client.post(
        f'{route}/grades',
        headers={'access-token':authorize_response.access_token}
    ).json().keys()) == list(StudentGrades().model_dump().keys())
    
    assert client.put(
        f'{route}/grades',
        headers={'access-token':authorize_response.access_token}
    ).status_code == status.HTTP_200_OK

    assert list(client.put(
        f'{route}/grades',
        headers={'access-token':authorize_response.access_token}
    ).json().keys()) == list(StudentGrades().model_dump().keys())

    assert client.delete(
        f'{route}/grades',
        headers={'access-token':authorize_response.access_token}
    ).status_code == status.HTTP_204_NO_CONTENT
    