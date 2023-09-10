# api-bridge-prototype
Bridge for connecting database and client using jwt security

# Table of contents

1. Purpose of the system
2. How to To use the api-bridge-prototype
3. File structure
4. Scopes
4. Registration and Authorization Flow

# Purpose of the system

The api-bridge-prototype is a middleware that connects a client application to a database server. It uses JSON Web Token (JWT) security to authenticate and authorize requests.

# How to To use the api-bridge-prototype
you first need to register your client application. This will give you a client ID and client secret that you will need to use to authorize requests. Once you have registered your client application, you can make CRUD requests to the database server through the API.

# File structure
    app/
    ├───routes/
    │   ├───course/
    │   ├───onesti/
    │   ├───payment/
    │   ├───staff/
    │   └───student/
    ├───security/
    └───test/
The `routes` directory contains the API endpoints. The `security` directory contains the code for JWT security. The `test` directory contains the unit tests for the API.

# Scopes
The api-bridge-prototype supports the following scopes:
#
| Scope | Description |
|---|---|
| `user-read-grades` | Allows the user to read grades. |
| `user-update-grades` | Allows the user to update grades. |
| `user-create-grades` | Allows the user to create grades. |
| `user-delete-grades` | Allows the user to delete grades. |
| `user-read-schedule` | Allows the user to read schedules. |
| `user-update-schedule` | Allows the user to update schedules. |
| `user-create-schedule` | Allows the user to create schedules. |
| `user-delete-schedule` | Allows the user to delete schedules. |
| `user-read-curriculum` | Allows the user to read curriculums. |
| `user-update-curriculum` | Allows the user to update curriculums. |
| `user-create-curriculum` | Allows the user to create curriculums. |
| `user-delete-curriculum` | Allows the user to delete curriculums. |
| `user-read-classroom` | Allows the user to read classrooms. |
| `user-update-classroom` | Allows the user to update classrooms. |
| `user-create-classroom` | Allows the user to create classrooms. |
| `user-delete-classroom` | Allows the user to delete classrooms. |
| `user-read-news` | Allows the user to read news. |
| `user-update-news` | Allows the user to update news. |
| `user-create-news` | Allows the user to create news. |
| `user-delete-news` | Allows the user to delete news. |
| `user-read-student-section` | Allows the user to read student sections. |
| `user-update-student-section` | Allows the user to update student sections. |
| `user-create-student-section` | Allows the user to create student sections. |
| `user-delete-student-section` | Allows the user to delete student sections. |

# Registration and Authorization Flow

### IMPORTANT NOTICE
### the registration url is only responsible for registering the client app. only the authorization server is only allowed to connect to this route

The api-bridge-prototype uses the OAuth 2.0 protocol for registration and authorization. To register your client application, you need to send a POST request to the /register endpoint. The request body should contain the following information:
```json
{
    name: "Your app name",
    app_type: "Your app type",
    role: "Your app role",
    scope: "The scopes your app needs to access",
}
```
- `name`: Name of the application.
- `app_type`: Type of the application.
- `role`: role of the application.
- `scope`: scopes that the apps need in the api and database.

after the request is completed the response body will contain
```json
{
    client_id: "Your client ID",
    client_secret: "Your client secret",
    scope: "The scopes your app needs to access",
}
```
- `client_id`: A unique identifier for your client application.
- `client_secret`: A secret key that will be used to sign requests.
- `scope`: The scopes that your client application needs to access.

Once your client application has been registered, you can request an access token by sending a POST request to the `/authorize` endpoint. The request body should contain the following information:

```json
{
    access_token: "The access token that you can use to communicate with the resource server."
    refresh_token: "The refresh token that you can use to refresh the main token."
    token_type: "The type of token."
    scope: "The scopes that the token grants."
}
```

# Example of connecting to the API

1. Create two constants, `registrationUrl` and `authorizationUrl`, to store the URLs of the registration and authorization routes.

**javascript**
```javascript 
const registrationUrl = "https://api.example.com/v1/security/register";
const authorizationUrl = "https://api.example.com/v1/security/authorization";
```
```python
registrationUrl = "https://api.example.com/v1/security/register"
authorizationUrl = "https://api.example.com/v1/security/authorization"
```
### IMPORTANT NOTICE
### the registration url is only responsible for registering the client app. only the authorization server is only allowed to connect to this route
2. Create a `POST` request to the `registrationUrl` with the following headers:
- **gateway-password: your-gateway-password**
```javascript
const response = await fetch(registrationUrl, {
    method: "POST",
    headers: {
      "gateway-password": "your-gateway-password",
    },
    body: JSON.stringify({
      name: "Your app name",
      app_type: "Your app type",
      role: "Your app role",
      scope: "The scopes your app needs to access",
    }),
});
```
```python
response = requests.post(registrationUrl, 
    headers={"gateway-password": "your-gateway-password"}, 
    json={
    "name": "Your app name",
    "app_type": "Your app type",
    "role": "Your app role",
    "scope": "The scopes your app needs to access",
})
```
```javascript
if (response.ok) {
    const data = await response.json();
    return data;
} else {
    throw new Error(response.statusText);
}
```
```python
if response.status_code == 200:
    return response.json()
else:
    raise Exception(response.reason)
```
The `gateway-password` header is used to authenticate the request. The `name`, `app_type`, `role`, and `scope` properties are used to register the app.

Create another request to handle the authorization request. make a `POST` request to the `authorizationUrl` with the following headers:
```javascript
const authorize = async () => {
  const response = await fetch(authorizationUrl, {
    method: "POST",
    headers: {
      "client-credentials": "your-client-credentials",
    },
    body: JSON.stringify({
      client_id: "Your client ID",
      client_secret: "Your client secret",
      scope: "The scopes your app needs to access",
    }),
});
```
```python
response = requests.post(authorizationUrl, 
    headers={"client-credentials": "your-client-credentials"}, 
    json={
    "client_id": "Your client ID",
    "client_secret": "Your client secret",
    "scope": "The scopes your app needs to access",
})
```
The `client-credentials` header is used to authenticate the request. The `client_id` and `client_secret` properties are used to authorize the app. The `scope` property is used to specify the scopes that the app needs to access.
```javascript
if (response.ok) {
    const data = await response.json();
    return data;
} else {
    throw new Error(response.statusText);
}
};
```
```python
if response.status_code == 200:
    return response.json()
else:
    raise Exception(response.reason)
```
you can now access the gathered data 
```javascript
console.log("Client ID:", clientId);
console.log("Access token:", accessToken);
```

# security

# test

# routes

