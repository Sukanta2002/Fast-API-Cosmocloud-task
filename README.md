# Cosmocloud Task FastAPI

Cousmocloud task for creating an API using FastAPI

**BASE URL:** `https://fast-api-cosmocloude-task.onrender.com/` 

## API Endpoints

### 1. Create a new student
- **URL:** `/api/students/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "name": "Demo",
        "age": 23,
        "address": {
            "city": "Demo-City"
            "country": "Demo-Country",
        }
        
    }
    ```
- **Response:**
    ```json
    {
        "id": "student-ID"
    }
    ```


### 2. Get all students
- **URL:** `/api/students/`
- **Method:** `GET`
- **Query students**: `/api/students/?country='Demo-country'&age=22`
- **Response:**
    ```json
    {
        "data" : [
            {
               "name": "Demo",
                "age": 23
            },
            {
               "name": "Demo",
                "age": 23
            }
        ]
    }
    ```

### 3. Get student by ID
- **URL:** `/api/students/{id}`
- **Method:** `GET`

- **Response:**
    ```json
    {
        "name": "Demo",
        "age": 23,
        "address": {
            "city": "Demo-City"
            "country": "Demo-Country",
        }
    }
    ```

### 4. Update student by ID
- **URL:** `/api/students/{id}`
- **Method:** `PATCH`
- **Request Body:**
    ```json
    {
        "name": "Demo",
        "age": 23,
        "address": {
            "city": "Demo-City"
            "country": "Demo-Country",
        }
        
    }
    ```
- **Response:** `No Content Code: 204`


### 5. Delete student by ID
- **URL:** `/api/students/{id}`
- **Method:** `DELETE`

- **Response:** `Code: 200`
