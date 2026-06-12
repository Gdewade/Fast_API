from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open("patient.json","r") as f:
        data=json.load(f)
        return data


@app.get("/greeting")
def greeting():
    return {"Greeting":"Hello World"}

@app.get("/view")
def view():         # for all patient information
    data = load_data()
    return data

# Path parameter : for particular profile information

@app.get("/patient/{patient_id}")
def patient(patient_id: int):
    data = load_data()

    for patient in data:
        if patient["id"] == patient_id:
            return patient

    # return {"message": "Patient not found"}
    raise HTTPException(status_code =404,details="patient not founds")  # to provide proper status code with message


