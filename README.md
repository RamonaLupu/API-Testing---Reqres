# API-Testing---Reqres


The API is available at `https://reqres.in`

## Endpoints ##

### List users - Get all users ###

GET `/api/users?page=2`

Returns a list of users.

Status code = 200


### Single user - Get user ###

GET `/api/users/2`

Returns the user whit "id" = 2.

Status code = 200


### Single user - Get user inexistent ###

GET `/api/users/23`

Returns {} 

Status code = 404


### List "resource" ###

GET `/api/unknown`

Status code = 200


### Single "resource" ###

GET `/api/unknown/2`

Status code = 200


### Single "resource" - Not found ###

GET `/api/unknown/23`

Status code = 404


### Create ###

POST `/api/users`

The request body needs to be in JSON format and include the following properties:

- name - String
- job - String

 Example

 ```
 {
    "name": "morpheus",
    "job": "leader"
}
 ```

Status code = 201.


### Update ###

PUT `/api/users/2`

The request body needs to be in JSON format and include the following properties:

- name - String
- job - String

 Example

 ```
 {
    "name": "morpheus",
    "job": "zion resident"
}
 ```
Update an existing order. 

Status code = 200


### Update user ###

PATCH `/api/users/2`

The request body needs to be in JSON format and include the following properties:

- name - String
- job - String

 Example

 ```
 {
    "name": "morpheus",
    "job": "zion resident"
}
 ```
Update an existing order. 

Status code = 200


### Delete ###

DELETE `/api/users/2`

Delete an existing user.

The request body needs to be empty.

Status code = 204


## Register - successful ##

POST `/api/register`

The request body needs to be in JSON format and include the following properties:

 - `email` - String
 - `password` - String

 Example

 ```
 {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
 ```

The response body will contain an id and one token. 

Status code = 200


## Register - unsuccessful ##

POST `/api/register`

The request body needs to be in JSON format and include the following properties:

 - `email` - String

 Example

 ```
 {
    "email": "sydney@fife"
}
 ```

The response body will contain the error: "Missing password". 

Status code = 400


## Login - successful ##

POST `/api/login`

The request body needs to be in JSON format and include the following properties:

 - `email` - String
 - `password` - String

 Example

 ```
 {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
 ```

The response body will contain an token. 

Status code = 200


## Login - unsuccessful1 ##

POST `/api/login`

The request body needs to be in JSON format and include the following properties:

 - `email` - String

 Example

 ```
 {
    "email": "peter@klaven"
}
 ```

The response body will contain the error: "Missing password" . 

Status code = 400


## Login - unsuccessful2 ##

POST `/api/login`

The request body needs to be in JSON format and include the following properties:

 - `password` - String

 Example

 ```
 {
    "password": "lup"
}
 ```

The response body will contain the error: "Missing email or username"

Status code = 400


### Delayed response ###

GET `/api/users?delay=3`

Status code = 200
