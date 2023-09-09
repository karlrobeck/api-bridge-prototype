from ..main import app
from fastapi.testclient import TestClient
from os import getenv
from ..security import auth

route = f"/{getenv('API_VERSION')}/security"

client = TestClient(app)

API_TOKEN = {}

def test_route():

    #REGISTER ROUTE
    register_response = client.post(
        f'{route}/register',
        headers={"gateway-password":getenv('GATEWAY_SECRET_KEY')},json={
        "name": "string",
        "app_type": "string",
        "role": "string",
        "scope": "string"
        }
    )

    assert register_response.status_code == 200
    assert list(register_response.json().keys()) == ['client_id','client_secret','client_credentials']

    print('\nREGISTER ROUTE: PASSED')

    #AUTHORIZATION ROUTE
    authorize_response = client.post(
        f'{route}/authorize',
        headers={'client-credentials':register_response.json()['client_credentials']},
        json={
            "client_credentials": register_response.json()['client_credentials'],
            "response_type": "json",
            "state": "string",
            "scope": "string"
        }
    )
    assert authorize_response.status_code == 200,'test'
    assert list(authorize_response.json().keys()) == ['access_token','refresh_token','scope','token_type']

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
    
