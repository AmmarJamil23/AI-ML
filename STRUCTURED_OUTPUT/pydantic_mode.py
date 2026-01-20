from pydantic import BaseModel, EmailStr, Field
from typing  import Optional

class Student(BaseModel):

    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=4)

new_student = {'name': 'Ammar','age': '22', 'email': 'ammar@gmail.com', 'cgpa': 3.99}

student = Student(**new_student)

print(student)

print(type(student))