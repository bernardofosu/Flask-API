# Most Used HTTP Status Codes and Use Cases

## 1. 200 OK
- **Use Case**: The request has been successfully processed and the response contains the requested data.
- **Example**: A GET request to `/movies` returns a list of movies.

## 2. 201 Created
- **Use Case**: The request has been successfully processed, and a new resource has been created.
- **Example**: A POST request to `/movies` creates a new movie in the database.

## 3. 204 No Content
- **Use Case**: The request was successful, but there is no content to return (used for DELETE requests).
- **Example**: A DELETE request to `/movies/{id}` successfully deletes a movie, but there is no data to return.

## 4. 400 Bad Request
- **Use Case**: The request is malformed or contains invalid data. This can be due to missing fields, incorrect format, or other issues with the request.
- **Example**: A POST request to create a movie without providing a required field like `title`.

### Difference between 400 (Bad Request) and 404 (Not Found)

#### 400 Bad Request:
- **When to use**: The problem is with the request itself (e.g., invalid input, missing fields, incorrect format).
- **Example**: A client sends a POST request to create a movie, but the `title` field is missing or the `release_year` is not an integer.
- **Response**: `400 Bad Request` and a message explaining the error.

#### 404 Not Found:
- **When to use**: The requested resource does not exist on the server, even though the request is valid.
- **Example**: A client requests a movie by ID, but the movie with that specific ID does not exist in the database.
- **Response**: `404 Not Found` with a message indicating that the resource could not be found.

## 5. 401 Unauthorized
- **Use Case**: The client needs to authenticate to access the requested resource.
- **Example**: A client tries to access a protected resource without providing valid authentication credentials.

## 6. 403 Forbidden
- **Use Case**: The server understood the request, but the client does not have permission to access the resource.
- **Example**: A client is logged in but tries to access a restricted area they do not have permission for.

## 7. 500 Internal Server Error
- **Use Case**: The server encountered an unexpected condition that prevented it from fulfilling the request.
- **Example**: The server has a bug or an issue with the database connection.

## 8. 503 Service Unavailable
- **Use Case**: The server is temporarily unable to handle the request due to overload or maintenance.
- **Example**: A server is down for maintenance or experiencing high traffic.

---

### Summary:
- **400 (Bad Request)**: Use when the issue is with the request itself (e.g., missing or invalid data).
- **404 (Not Found)**: Use when the requested resource cannot be found on the server.

The difference between **400 (Bad Request)** and **404 (Not Found)** is based on the nature of the error. 
- **400** indicates that the request itself is faulty, while 
- **404** indicates that the resource could not be found, even if the request itself was valid.
