from pydantic import BaseModel,Field
from typing import Annotated

class Person(BaseModel):
    name:Annotated[str,Field()]
    age:Annotated[int,Field()]
    salary:Annotated[float,Field()]

new_person=Person(name="Gayatri",age=21,salary=50000)
print(new_person)
print("--------------------------------------------------------")
print(new_person.name)
print(new_person.age)
print(new_person.salary)