# UDPlatforms Assignment
## Nowfel Mashnoor
##### Phone: 01826636115, E-mail: nmmashnoor@gmail.com

## Description

**Language:** Python

**Database:** SQLite

**Framework**: aiohttp

## Getting Started

**Docker**

To run the project set all the environment to a `.env` file. To run the project locally you need to setup `docker` and `docker-compose`.
 Then simply do `docker-compose up --build` to run the project. 



**From Source**
```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```


Then verify the deployment by navigating to your server address in
your preferred browser.

```sh
http://localhost:8030/
```




### Base Url:
```
https://api-dev.evaly.com.bd/rate-limiter/api/v1
```

## API USAGE
### User Add
```http
POST /v1/user
```
**Request Body**

**Type:** 
JSON

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `first_name` | `string` | **Required** |
| `last_name` | `string` | **Required** |
| `user_type` | `string` | **Required** |
| `street` | `int` | **Required** |
| `city` | `string` | **Required** |
| `state` | `string` | **Required** |
| `zip` | `int` | **Required** |
| `parent_id` | `int` | **Required if user_type='child'** |
**Note**: user_typer = ['parent', 'child']

**Response**
```json=
{
  "success": true,
  "message": "User created successfully",
  "data": {
    "id": 4,
    "first_name": "nowfel",
    "last_name": "Mashnoor",
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


**Response**
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

**Response**
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

