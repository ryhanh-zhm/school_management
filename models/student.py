from models.user import User
from utils.data_manager import load_data, save_data

class Student(User):
    def __init__(self, username, parent_username):
        super().__init__(username, "student")
        self.parent_username = parent_username
        self.classroom_id = None
        self.grades = {}
        self.disciplinary_records = []

    def assign_classroom(self, classroom_id):
        self.classroom_id = classroom_id
        self._save()

    def add_grade(self, course_id, term, midterm, activity, quiz, final):
        if course_id not in self.grades:
            self.grades[course_id] = {}
        self.grades[course_id][term] = {
            "midterm": midterm,
            "activity": activity,
            "quiz": quiz,
            "final": final,
            "total": (midterm + activity + quiz) * 1 + final * 2
        }
        self._save()

    def add_disciplinary_record(self, record_id):
        records = load_data("disciplinary.json")
        if record_id not in records:
            raise ValueError("Disciplinary record not found")
        self.disciplinary_records.append(record_id)
        self._save()

    def view_dashboard(self):
        return {
            "username": self.username,
            "classroom_id": self.classroom_id,
            "grades": self.grades,
            "disciplinary_records": self.disciplinary_records
        }

    def _save(self):
        # Save to users.json (inherited from User)
        super()._save()
        # Save to students.json separately
        students = load_data("students.json")
        students[self.id] = self.__dict__
        save_data("students.json", students)
        # Debug: Confirm save
        with open("data/students.json", "r") as f:
            print(f"Students.json content after save: {f.read()}")