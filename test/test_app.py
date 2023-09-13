import os
from app.main import app
from app.security.schemas import ClientInfo,Credentials,AuthorizeBody,AuthorizationData
from fastapi.testclient import TestClient
from fastapi import status

absolute_path = '/'.join(os.path.dirname(__file__).split('/')[:-1])

client = TestClient(app)

def get_access_token(scope:str=""):

    register_response = Credentials(**client.post(
        url='v1/security/register',
        headers={'gateway-password':os.getenv('GATEWAY_SECRET_KEY')},
        json=ClientInfo(
            name="Test Application",
            app_type="Testing",
            role="development",
            scope=scope
        ).model_dump()
    ).json())

    return AuthorizationData(**client.post(
        url='v1/security/authorize',
        headers={'client-credentials':register_response.client_credentials},
        json=AuthorizeBody(
            response_type='json',
            state='random string',
            scope=register_response.scopes,
        ).model_dump()
    ).json())


def test_routes():

    methods = ['post','get','put','delete']

    routes = [x for x in os.listdir(os.path.join(absolute_path,'app/routes')) if x not in ['api.py','__init__.py','__pycache__']]

    scopes = []
    route_endpoints = []
    for r in routes:
        endpoints = [os.path.splitext(x)[0] for x in os.listdir(os.path.join(absolute_path,f'app\\routes\\{r}')) if x not in ['api.py','__init__.py','__pycache__','schemas.py']]
        for e in endpoints:
            for m in methods:
                scopes.append(f'user-{m}-{r}-{e}')
            route_endpoints.append(f'v1/{r}/{e}')

    scopes = ' '.join(scopes)

    authorization_credentials = get_access_token(scopes)

    for url in route_endpoints:
        print(url)
        assert client.get(
            url=url,
            headers={'access-token':authorization_credentials.access_token}
        ).status_code == status.HTTP_200_OK

        assert client.post(
            url=url,
            headers={'access-token':authorization_credentials.access_token}
        ).status_code == status.HTTP_201_CREATED

        assert client.put(
            url=url,
            headers={'access-token':authorization_credentials.access_token}
        ).status_code == status.HTTP_205_RESET_CONTENT

        assert client.delete(
            url=url,
            headers={'access-token':authorization_credentials.access_token}
        ).status_code == status.HTTP_204_NO_CONTENT

def test_security():

    register_response = client.post(
        url='v1/security/register',
        headers={'gateway-password':os.getenv('GATEWAY_SECRET_KEY')},
        json=ClientInfo(
            name="Test Application",
            app_type="Testing",
            role="development",
            scope="user-get-course-info"
        ).model_dump()
    )

    assert register_response.status_code == status.HTTP_201_CREATED

    register_response = Credentials(**register_response.json())

    authorization = client.post(
        url='v1/security/authorize',
        headers={'client-credentials':register_response.client_credentials},
        json=AuthorizeBody(
            response_type='json',
            state='random string',
            scope=register_response.scopes,
        ).model_dump()
    )

    assert authorization.status_code == status.HTTP_200_OK
