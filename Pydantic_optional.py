from pydantic import BaseModel,Field
from typing import Annotated ,Optional

class StudentInfo(BaseModel):
    name:Annotated[str,Field(max_length=50,min_length=3,description="Student Name")]
    age:Annotated[Optional[int],Field(description="Student Age")]=None

stud1=StudentInfo(name="Gayatri")
print(stud1)
print("---------------------------")
stud2=StudentInfo(name="Gayatri",age=21)
print(stud2)