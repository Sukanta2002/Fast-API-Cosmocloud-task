from fastapi import APIRouter, status
from models.student_model import Student ,UpdateStudent
from configs.database import collection
from bson import ObjectId
from schemas.student_schema import student_to_dict, students_to_list, student_model_to_dict
from pydantic.v1.utils import deep_update

router = APIRouter(prefix="/api/students")


# Router for adding new students
@router.post("/", status_code=status.HTTP_201_CREATED)
def post_students(student: Student) -> dict:
    res =  collection.insert_one(student_model_to_dict(student))
    # print(res.acknowledged)
    # print(res.inserted_id)
    return  {
        "id" :str(res.inserted_id)
    }


# Route for getting students
@router.get("/")
def get_all_students(country: str = None, age: int = None) -> dict:

    if age is not None and country is not None:

        db_students = collection.find({"age": age, "address.country": country},{"_id": 0,"address": 0})
    elif age is not None:

        db_students = collection.find({"age": age},{"_id": 0,"address": 0})
    
    elif country is not None:

        db_students = collection.find({ "address.country": country.lower()},{"_id": 0,"address": 0})
    else:
        db_students = collection.find({},{"_id": 0,"address": 0})
    students = students_to_list(db_students)
    return {
        "data": students
    }


# route for getting deails of one student by their id
@router.get("/{id}")
def get_all_students(id: str) -> dict:
    db_student = collection.find_one({"_id": ObjectId(id)},{"_id": 0})
    student = student_to_dict(db_student)
    return student


# Update the student details
@router.patch("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def update_student(id: str,student : UpdateStudent | None = None):
    upd_stu = student.model_dump(exclude_unset=True)
    db_student = collection.find_one({"_id": ObjectId(id)})
    stu = student_to_dict(db_student)
    stu = deep_update(stu,upd_stu)
    collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": {
        "name": stu["name"].lower(),
        "age": stu["age"],
        "address": {
            "city": stu["address"]["city"].lower(),
            "country": stu["address"]["country"].lower()
        }
    }})
    return {}

# delete the student
@router.delete("/{id}")
def delete_student(id : str):
    collection.find_one_and_delete({"_id": ObjectId(id)})
    return {}
