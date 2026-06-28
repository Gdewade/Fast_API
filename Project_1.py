from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get("/")
def home():
    return {"message": "Welcome"}

@app.post("/users")
def create_user(user: User):
    return user

@app.put("/users/{id}")
def update_user(id: int, user: User):
    return {"id": id, "updated_user": user}

@app.delete("/users/{id}")
def delete_user(id: int):
    return {"message": f"User {id} deleted"}