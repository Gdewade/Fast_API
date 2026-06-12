from pydantic import BaseModel,Field
from typing import Annotated

class StudentInfo(BaseModel):

    name:Annotated[str,Field(min_length=3,max_length=50,description="Student Name")]
    age:Annotated[int,Field(ge=0,lt=100,description="Student age")]
    indian:Annotated[bool,Field(description="Whether the student is indian")]
    cgpa:Annotated[float,Field(ge=5,lt=10,description="CGPA of student")]

stud1=StudentInfo(name="Gayatri",age=21,indian=0,cgpa=8.1)
print(stud1)