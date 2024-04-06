from pydantic import BaseModel

# Sub-Model for address
class Address(BaseModel):
    city: str
    country: str

# Main model student
class Student(BaseModel):
    name: str
    age: int
    address: Address


# Updared model for UpdateStudent class
class UpdatedAddress(BaseModel):
    city: str |None = None
    country: str|None = None



# for updated the student details
class UpdateStudent(BaseModel):
    name: str | None = None
    age : int | None = None
    address : UpdatedAddress | None = None

