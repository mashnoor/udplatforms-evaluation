# UDPlatforms Assignment

Hosted in: https://evaluation.mashnoor.com

Insomnia File: https://drive.google.com/file/d/1IdbL2UMPsIFwq3El3OViEoJxrnN_sktm/view?usp=sharing

## Description

**Language:** Python

**Database:** SQLite

**Framework**: aiohttp

## Getting Started

**Using Docker**

To run the project set all the environment to a `.env` file. To run the project locally you need to setup `docker` and `docker-compose`.
 Then simply do `docker-compose up --build` to run the project. 



**Using Source**
```sh=
git clone https://github.com/mashnoor/udplatforms-evaluation.git
cd udplatforms-evaluation
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd src/
python main.py
```


Then verify the deployment by navigating to:

```sh
http://localhost:8030/
```


### Base URL:
```
https://evaluation.mashnoor.com/api

or

http://localhost:8030/api
```

## API USAGE
### User Add
```http
POST /v1/user
```
**Headers**

| Parameter | Value | 
| :--- | :--- 
| `Content-Type` | `application/json` | 
**Request Body**

**Type:** 
JSON

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `first_name` | `string` | **Required** |
| `last_name` | `string` | **Required** |
| `user_type` | `string` | **Required** |
| `street` | `int` | **Optional if user_type='child'** |
| `city` | `string` | **Optional if user_type='child'** |
| `state` | `string` | **Optional if user_type='child'** |
| `zip` | `int` | **Optional if user_type='child'** |
| `parent_id` | `int` | **Required if user_type='child'** |
**Note**: user_typer = ['parent', 'child']

**Request example**
```json=
curl --request POST \
  --url https://evaluation.mashnoor.com/api/v1/user \
  --header 'Content-Type: application/json' \
  --data '{
	"first_name":"dsds",
	"last_name": "sdsdfs",
	"user_type": "parent",
	"street": "Banasree",
	"city" : "Dhaka",
	"state" : "Dhaka",
	"zip" : 1219
}''
```

**Response Example**
```json=
{
  "success": true,
  "message": "User created successfully",
  "data": {
    "id": 4,
    "first_name": "dsds",
    "last_name": "sdsdfs",
    "address": {
      "street": "Banasree",
      "zip": 1219,
      "city": "Dhaka",
      "state": "Dhaka"
    },
    "type": "parent"
  }
}
```
### User Update
```http
PUT /v1/user?id=2
```
**Request Body**

**Type:**
JSON

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `first_name` | `string` | **Optional** |
| `last_name` | `string` | **Optional** |
| `street` | `int` | **Optional** |
| `city` | `string` | **Optional** |
| `state` | `string` | **Optional** |
| `zip` | `int` | **Optional** |
| `parent_id` | `int` | **Optional** |


**Request example**
```json=
curl --request PUT \
  --url 'https://evaluation.mashnoor.com/api/v1/user?id=1' \
  --header 'Content-Type: application/json' \
  --data '{
	"first_name":"dd",
	"last_name": "Mashnoor",
	"user_type": "parent",
	"street": "Banasree",
	"city" : "Dhaka",
	"zip" : 1218
}'
```

**Response Example**
```json=
{
  "success": true,
  "message": "User updated successfully",
  "data": {
    "id": 8,
    "first_name": "dd",
    "last_name": "Mashnoor",
    "address": {
      "street": "Banasree",
      "zip": 1218,
      "city": "Dhaka",
      "state": "Dhaka"
    }
  }
}
```

### User Delete
```http
DELETE /v1/user?id=2
```

**Request example**
```json=
curl --request DELETE \
  --url 'https://evaluation.mashnoor.com/api/v1/user?id=1'
```

**Respons example**
```json=
{
  "success": true,
  "message": "User updated successfully",
  "data": {
    "id": 8,
    "first_name": "dd",
    "last_name": "Mashnoor",
    "address": {
      "street": "Banasree",
      "zip": 1218,
      "city": "Dhaka",
      "state": "Dhaka"
    }
  }
}
```

