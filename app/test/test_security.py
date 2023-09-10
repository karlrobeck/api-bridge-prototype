from ..main import app
from fastapi.testclient import TestClient
from os import getenv
from ..security import auth
from ..security.types import Credentials,ClientInfo,AuthorizeBody,AuthorizationData
route = f"/{getenv('API_VERSION')}/security"

client = TestClient(app)

def test_route():

    #REGISTER ROUTE
    register_response = client.post(
        f'{route}/register',
        headers={"gateway-password":getenv('GATEWAY_SECRET_KEY')},
        json=ClientInfo(
            name="Test Client",
            app_type="basic",
            role="basic",
            scope="user-read-grades user-update-grades user-create-grades user-delete-grades"
        ).model_dump()
    )

    assert register_response.status_code == 201
    assert list(register_response.json().keys()) == list(Credentials().model_dump().keys())

    print('\nREGISTER ROUTE: PASSED')

    #AUTHORIZATION ROUTE
    authorize_response = client.post(
        f'{route}/authorize',
        headers={'client-credentials':register_response.json()['client_credentials']},
        json={
            "response_type": "json",
            "state": "string",
            "scope": "string"
        }
    )
    assert authorize_response.status_code == 200
    assert list(authorize_response.json().keys()) == list(AuthorizationData().model_dump().keys())

    print('AUTHORIZE ROUTE: PASSED')

def test_auth_function():
    
    test_string:str = 'Test String'
    test_token_data:dict = {'test 1':1,'test 2':2,'test 3':3,}
    #verify / encrypt hash
    assert type(auth.get_hash(test_string)) == str
    assert auth.verify_hash(
        test_string,
        auth.get_hash(test_string)
    )
    
    print('VERIFY / ENCRYPT HASH: PASSED')
    
    #encode / decode token
    
    assert type(auth.create_token(test_token_data)) == str
    assert type(auth.decode_token(auth.create_token(test_token_data))) == dict

    print('ENCODE / DECODE TOKEN: PASSED')

    #encode / decode b64
    assert type(auth.encode_b64(test_string)) == str
    assert type(auth.decode_b64(auth.encode_b64(test_string))) == str
    
