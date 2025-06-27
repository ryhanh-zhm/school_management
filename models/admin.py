from models.user import User
from models.student import Student
from models.teacher import Teacher
from models.parent import Parent
from utils.data_manager import load_data, save_data
from models.report_card import ReportCard

class Admin(User):
    def __init__(self, username):
        super().__init__(username, "admin")

    def add_teacher(self, username):
        teacher = Teacher(username)
        teacher._save()
        return teacher

    def add_vice_principal(self, username):
        vp = User(username, "vice_principal")
        vp._save()
        return vp

    def view_all_letters(self):
        return load_data("letters.json")

    def issue_report_cards(self, term):
        students = load_data("students.json")
        classrooms = load_data("classrooms.json")
        for student in students.values():
            classroom = classrooms.get(student["classroom_id"], {})
            courses = classroom.get("courses", [])
            for course_id in courses:
                if course_id not in student["grades"] or term not in student["grades"][course_id]:
                    raise ValueError(f"Grades for {course_id} in term {term} not entered for student {student['username']}")
            report_card = ReportCard(student["id"], term)
            report_card.generate()