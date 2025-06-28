from models.user import User
from utils.data_manager import load_data

class Parent(User):
    def __init__(self, username, student_id):
        super().__init__(username, "parent")
        self.student_id = student_id

    def view_student_dashboard(self):
        students = load_data("students.json")
        student_data = students.get(self.student_id)
        if not student_data:
            raise ValueError("Student not found")
        return {
            "username": student_data["username"],
            "classroom_id": student_data.get("classroom_id"),
            "grades": student_data.get("grades", {}),
            "disciplinary_records": student_data.get("disciplinary_records", [])
        }