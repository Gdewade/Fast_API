from fastapi import FastAPI,Path
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
# def patient(patient_id: int):
def patient(patient_id=Path(...,description="ID of patient",example="P001")):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="Patient ID is not available")

    # for patient in data:
    #     if patient["id"] == patient_id:
    #         return patient

    # return {"message": "Patient not found"}
    # raise HTTPException(status_code =404,details="patient not founds")  # to provide proper status code with message


# Query parameter : when we want additional information 

@app.get("/sort")
def sort_patient(sort_by:str,
                 order:str):
    
    valid_fields=["height","weight","bmi","age"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail="Invalid Field Selection, please select from {valid_fields}")
    
    if order not in ["asc","desc"]:
        raise HTTPEXception(status_code=400,detail="Invalid order selection ,please select between asc and desc")
    
    data=load_data()
    
    sort_order=True if order == "desc" else False
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by),reverse=sort_order)

    return sorted_data

@app.get("/city")
def sort_city(city:str):

    valid_city=["Mumbai"]

    if city not in valid_city:
        raise HTTPException(status_code=400,detail="Invalid city selection")
    
    data=load_data()

    filtered_data= [patient 
                    for patient in data.values()
                    if patient.get("city") == city]

    return filtered_data

@app.get("/gender")
def sort_gender(gender:str):

    # valid=['Male','male']

    # if gender not in valid:
    #     raise HTTPException(status_code=400,detail="Invalid gender")
    
    data=load_data()

    print("Query gender:", gender)

    for patient in data.values():
        print("Patient gender:", patient.get("gender"))

    filtered_gender=[patient
                     for patient in data.values()
                     if patient.get("gender").lower() == gender.lower()]
    

    print("Result:", filtered_gender)
    return filtered_gender

# filtered_data = []

# for patient in data.values():

#     if patient.get("city") == city:

#         filtered_data.append(patient)

# return filtered_data

