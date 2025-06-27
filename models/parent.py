from models.user import User
from utils.data_manager import load_data

class Parent(User):
    def __init__(self, username, student_id):
        super().__init__(username, "parent")
        self.student_id = student_id

    def view_student_dashboard(self):
        students = load_data("students.json")
        student = students.get(self.student_id)
        if not student:
            raise ValueError("Student not found")
        return student["grades"], student["disciplinary_records"]
    