from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel): # Student Model
    roll_number: int
    name: str
    attendance: bool = False

students = [] # List of Students

@app.post("/students/")
async def create_student(student: Student):
    students.append(student)
    return student

@app.get("/students/")
async def get_students():
    return students

@app.get("/students/{roll_number}")
async def get_student(roll_number: int):
    for student in students:
        if student.roll_number == roll_number:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.put("/students/{roll_number}")
async def update_student(roll_number: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.roll_number == roll_number:
            updated_student.roll_number = roll_number
            students[index] = updated_student
            return updated_student
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{roll_number}")
async def delete_student(roll_number: int):
    for index, student in enumerate(students):
        if student.roll_number == roll_number:
            return students.pop(index)
    raise HTTPException(status_code=404, detail="Student not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)