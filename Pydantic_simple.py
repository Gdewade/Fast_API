from pydantic import BaseModel,Field
from typing import Annotated

class Person(BaseModel):
    name:str
    age:int
    salary:float

new_person=Person(name="Gayatri",age=21,salary=50000.1)
print(new_person)