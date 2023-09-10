from pydantic import BaseModel


class AuthorizeBody(BaseModel):
    """
    Body of the authorization request.

    Attributes:
        response_type: The type of response that the client expects.
        state: A random string that the client can use to prevent CSRF attacks.
        scope: The scopes that the client is requesting.
    """

    response_type: str = ""
    state: str = ""
    scope: str = ""


class AuthorizationData(BaseModel):
    """
    Data returned by the authorization server.

    Attributes:
        access_token: The access token.
        refresh_token: The refresh token.
        token_type: The type of token.
        scope: The scopes that the token grants.
    """

    access_token: str = ""
    refresh_token: str = ""
    token_type: str = ""
    scope: str = ""


class ClientInfo(BaseModel):
    """
    Client information.

    Attributes:
        name: The name of the client.
        app_type: The type of client.
        role: The role of the client.
        scope: The scopes that the client is authorized to use.
    """

    name: str = ""
    app_type: str = ""
    role: str = ""
    scope: str = ""


class ClientSecret(BaseModel):
    """
    Client secret.

    Attributes:
        name: The name of the client.
        signature: The signature of the client secret.
    """

    name: str = ""
    signature: str = ""


class Credentials(BaseModel):
    """
    Credentials for a client.

    Attributes:
        client_id: The client ID.
        client_secret: The client secret.
        client_credentials: The client credentials.
        scopes: The scopes that the client is authorized to use.
    """

    client_id: str = ""
    client_secret: str = ""
    client_credentials: str = ""
    scopes: str = ""