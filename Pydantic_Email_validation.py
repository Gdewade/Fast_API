from pydantic import BaseModel,Field,EmailStr
from typing import Annotated

class StudentInfo(BaseModel):

    name:Annotated[str,Field(min_length=3,max_length=50)]
    age:Annotated[int,Field(gt=0,lt=30)]
    email:Annotated[EmailStr,Field(description="Student email addresss")]


stud=StudentInfo(name="Gayatri",age=21,email="gayatri@gmail.com")
print(stud)
print("------------------------------------------------------------------")
# stud1=StudentInfo(name="Gayatri",age=21,email="gayatrigmail.com")
# print(stud)