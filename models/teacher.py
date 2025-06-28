from models.user import User
from models.student import Student
from utils.data_manager import load_data

class Teacher(User):
    def __init__(self, username):
        super().__init__(username, "teacher")
        self.courses = []

    def view_classes(self):
        classes = load_data("classrooms.json")
        return [c for c in classes.values() if any(course_id in self.courses for course_id in c["courses"])]

    def add_grade(self, student_id, course_id, term, midterm, activity, quiz, final):
        students = load_data("students.json")
        student_data = next((s for s in students.values() if s["id"] == student_id), None)
        if not student_data:
            raise ValueError("Student not found")
        if course_id not in self.courses:
            raise ValueError("Teacher not assigned to this course")
        student_obj = Student(student_data["username"], student_data["parent_username"])
        student_obj.id = student_data["id"]
        student_obj.classroom_id = student_data.get("classroom_id")
        student_obj.grades = student_data.get("grades", {})
        student_obj.disciplinary_records = student_data.get("disciplinary_records", [])
        student_obj.add_grade(course_id, term, midterm, activity, quiz, final)