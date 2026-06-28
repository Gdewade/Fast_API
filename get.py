from fastapi import FastAPI
import json

app=FastAPI()

def load_data():
    with open("students.json","r") as f:
        data=json.load(f)
        return data
    
@app.get("/view")
def view():
    data=load_data()
    return data

@app.get("/student/{student_id}")
def student(student_id:int):
    data=load_data()

    for student in data["students"]:
        if student["id"] == student_id:
            return student
        
    raise HTTPException(status_code=400,details="student not found")

