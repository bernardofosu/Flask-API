# ✅ FastAPI + Beanie + MongoDB Example

## 📁 Project Structure

```bash
fastapi-movies/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── database.py
│   ├── controllers.py
└── requirements.txt
```

## 📦 Install Required Packages

First, install FastAPI, Beanie, and Motor:

```bash
pip install fastapi[all] beanie motor
```

## 🗃️ Database Configuration (database.py)

```python
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.models import Movie

async def init_db():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(database=client.movies_db, document_models=[Movie])
```

## 🎬 Movie Model (models.py)

```python
from beanie import Document
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class Movie(Document):
    name: str = Field(..., max_length=100)
    description: str
    duration: int
    release_year: int
    genres: List[str]
    created_at: datetime = Field(default_factory=datetime.now)

    class Settings:
        collection = "movies"

    def duration_in_hours(self) -> float:
        return round(self.duration / 60, 2)

class MovieCreate(BaseModel):
    name: str
    description: str
    duration: int
    release_year: int
    genres: List[str]
```

## 🧑‍💻 Controllers (controllers.py)

```python
from fastapi import HTTPException
from app.models import Movie, MovieCreate

class MovieController:
    async def create_movie(self, movie_data: MovieCreate):
        existing_movie = await Movie.find_one(Movie.name == movie_data.name)
        if existing_movie:
            raise HTTPException(status_code=400, detail="Movie already exists")
        
        movie = Movie(**movie_data.dict())
        await movie.insert()
        return movie

    async def get_all_movies(self):
        return await Movie.find_all().to_list()

    async def get_movie(self, movie_id: str):
        movie = await Movie.get(movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        return movie

    async def delete_movie(self, movie_id: str):
        movie = await Movie.get(movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        await movie.delete()
        return {"message": "Movie deleted successfully"}
```

## 🚀 Routes (routes.py)

```python
from fastapi import APIRouter
from app.controllers import MovieController
from app.models import MovieCreate

movie_router = APIRouter()
controller = MovieController()

@movie_router.post("/", response_model=MovieCreate)
async def create_movie(movie_data: MovieCreate):
    return await controller.create_movie(movie_data)

@movie_router.get("/", response_model=list[MovieCreate])
async def get_all_movies():
    return await controller.get_all_movies()

@movie_router.get("/{movie_id}", response_model=MovieCreate)
async def get_movie(movie_id: str):
    return await controller.get_movie(movie_id)

@movie_router.delete("/{movie_id}")
async def delete_movie(movie_id: str):
    return await controller.delete_movie(movie_id)
```

## 🌟 Main Application (main.py)

```python
from fastapi import FastAPI
from app.routes import movie_router
from app.database import init_db

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()

app.include_router(movie_router, prefix="/api/v1/movies", tags=["Movies"])
```

## ✅ Run the Application

Make sure MongoDB is running locally:

```bash
mongod
```

Then, run FastAPI using uvicorn:

```bash
uvicorn app.main:app --reload
```

- API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- Movies API: [http://localhost:8000/api/v1/movies](http://localhost:8000/api/v1/movies)

## ✅ Example API Calls

### Create a Movie
```http
POST http://localhost:8000/api/v1/movies
Content-Type: application/json

{
  "name": "Inception",
  "description": "A mind-bending thriller.",
  "duration": 148,
  "release_year": 2010,
  "genres": ["Sci-Fi", "Thriller"]
}
```

### Get All Movies
```http
GET http://localhost:8000/api/v1/movies
```

### Get a Single Movie
```http
GET http://localhost:8000/api/v1/movies/{movie_id}
```

### Delete a Movie
```http
DELETE http://localhost:8000/api/v1/movies/{movie_id}
```

