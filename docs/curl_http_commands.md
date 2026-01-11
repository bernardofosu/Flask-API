# 📌 cURL Commands for Interacting with a REST API

This markdown file contains useful cURL commands to interact with an API using different HTTP methods. It includes both Linux/macOS and Windows commands. 🚀

## 🔹 GET Request (Retrieve Data)

### Linux/macOS 🐧
```sh
curl -X GET http://127.0.0.1:5000/api/v1/movies/ -H "Content-Type: application/json"
```

### Windows 🪟
```sh
curl -X GET "http://127.0.0.1:5000/api/v1/movies/" -H "Content-Type: application/json"
```

## 🔹 GET a Single Movie

### Linux/macOS 🐧
```sh
curl -X GET http://127.0.0.1:5000/api/v1/movies/{movie_id} -H "Content-Type: application/json"
```

### Windows 🪟
```sh
curl -X GET "http://127.0.0.1:5000/api/v1/movies/{movie_id}" -H "Content-Type: application/json"
```

## 🔹 POST Request (Create a New Movie)

### Linux/macOS 🐧
```sh
curl -X POST http://127.0.0.1:5000/api/v1/movies/ \
     -H "Content-Type: application/json" \
     -d '{"title": "Inception", "release_year": 2010, "genres": ["Sci-Fi", "Thriller"]}'
```

### Windows 🪟
```sh
curl -X POST "http://127.0.0.1:5000/api/v1/movies/" ^
     -H "Content-Type: application/json" ^
     -d "{\"title\": \"Inception\", \"release_year\": 2010, \"genres\": [\"Sci-Fi\", \"Thriller\"]}"
```

## 🔹 PUT Request (Update an Existing Movie)

### Linux/macOS 🐧
```sh
curl -X PUT http://127.0.0.1:5000/api/v1/movies/{movie_id} \
     -H "Content-Type: application/json" \
     -d '{"title": "Interstellar", "release_year": 2014}'
```

### Windows 🪟
```sh
curl -X PUT "http://127.0.0.1:5000/api/v1/movies/{movie_id}" ^
     -H "Content-Type: application/json" ^
     -d "{\"title\": \"Interstellar\", \"release_year\": 2014}"
```

## 🔹 DELETE Request (Remove a Movie)

### Linux/macOS 🐧
```sh
curl -X DELETE http://127.0.0.1:5000/api/v1/movies/{movie_id}
```

### Windows 🪟
```sh
curl -X DELETE "http://127.0.0.1:5000/api/v1/movies/{movie_id}"
```

## 🛠️ Explanation of cURL Options

| Option | Description |
|--------|-------------|
| `-X` | Specifies the HTTP method (GET, POST, PUT, DELETE, etc.). |
| `-H` | Adds a header to the request, e.g., `-H "Content-Type: application/json"`. |
| `-d` | Sends data in a request body (used with POST and PUT). |
| `-D` | Saves response headers to a file. |
| `-v` | Enables verbose mode to see request and response details. |
| `-i` | Includes response headers in the output. |
| `-o <filename>` | Writes output to a file instead of the terminal. |

📌 **Note:** Replace `{movie_id}` with the actual movie ID in the API. Happy coding! 🎬🚀

