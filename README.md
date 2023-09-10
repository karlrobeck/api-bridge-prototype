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

- `user-read-grades`
- `user-update-grades`
- `user-create-grades`
- `user-delete-grades`
- `user-read-schedule`
- `user-update-schedule`
- `user-create-schedule`
- `user-delete-schedule`
- `user-read-curriculum`
- `user-update-curriculum`
- `user-create-curriculum`
- `user-delete-curriculum`
- `user-read-classroom`
- `user-update-classroom`
- `user-create-classroom`
- `user-delete-classroom`
- `user-read-news`
- `user-update-news`
- `user-create-news`
- `user-delete-news`
- `user-read-student-section`
- `user-update-student-section`
- `user-create-student-section`
- `user-delete-student-section`

# Registration and Authorization Flow

The api-bridge-prototype uses the OAuth 2.0 protocol for registration and authorization. To register your client application, you need to send a POST request to the /register endpoint. The request body should contain the following information:

- `client_id`: A unique identifier for your client application.
- `client_secret`: A secret key that will be used to sign requests.
- `scope`: The scopes that your client application needs to access.

Once your client application has been registered, you can request an access token by sending a POST request to the `/authorize` endpoint. The request body should contain the following information:

