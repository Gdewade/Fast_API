from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal,Optional
import json

app = FastAPI()

class Patient(BaseModel):
    id:Annotated[str,Field(...,description="ID of the patient",examples=["P001"])]
    name:Annotated[str,Field(...,description="Name of the patient")]
    city:Annotated[str,Field(...,description="city where patient is living")]
    age:Annotated[int,Field(...,gt=0,lt=120,description="Age of the patient")]
    gender:Annotated[Literal["male","Female","others"],Field(...,description="Gender of the patient")]
    height:Annotated[float,Field(...,gt=0,description="Height of the patient in mtrs")]
    weight:Annotated[float,Field(...,gt=0,description="Weight of the patient in kgs")]
    
    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<18.5:
            return "Underweight"
        elif self.bmi<25:
            return "Normal"
        elif self.bmi<30:
            return "Normal"
        else:
            return "Obese"

class PatientUpdate(BaseModel):
    name:Annotated[Optional[str],Field(default=None)]
    city:Annotated[Optional[str],Field(default=None)]
    age:Annotated[Optional[int],Field(default=None)]
    gender:Annotated[Optional[Literal["male","female","other"]],Field(default=None)]
    height:Annotated[Optional[float],Field(default=None,gtf=0)]
    weight:Annotated[Optional[float],Field(default=None,gt=0)]

    
def load_data():
    with open("patient.json","r") as f:
        data=json.load(f)
        return data
    
def save_data(data):
    with open("patient.json","w") as f:
        json.dump(data,f)

@app.get("/")
def view():
    return {"message":"jai ganesh"}


@app.get("/view")
def view():
    data=load_data()
    return data
   
@app.put("edit/{patient_id}")
def update_patient(patient_id:str,patient_update:PatientUpdate):

    data=load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404,detail="Patient not found")
    
    existing_patient = data[patient_id]

    updated_patient = patient_update.model_dump(exclude_unset=True)

    for key,value in updated_patient.items():
        existing_patient[key]=value

    existing_patient["id"] = patient_id

    patient_pydantic_obj = Patient(**existing_patient)

    existing_patient = patient_pydantic_obj.model_dump(exclude="id")

    data[patient_id] = existing_patient

    save_data(data)

    return JSONResponse(status_code=200,content={"message":"Patient Updated"})

