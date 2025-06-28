from models.user import User
from models.teacher import Teacher
from models.vice_principal import VicePrincipal
from models.student import Student
from models.parent import Parent
from utils.data_manager import load_data, save_data

class Admin(User):
    def __init__(self, username):
        super().__init__(username, "admin")

    def add_teacher(self, username):
        teacher = Teacher(username)
        teacher._save()
        return teacher

    def add_vice_principal(self, username):
        vp = VicePrincipal(username)
        vp._save()
        return vp

    def issue_report_cards(self, term):
        students = load_data("students.json")
        report_cards = load_data("report_cards.json")
        for student_id, student_data in students.items():
            if student_data["grades"]:
                report_card = {
                    "student_id": student_id,
                    "term": term,
                    "grades": student_data["grades"]
                }
                report_cards[f"{student_id}_{term}"] = report_card
        save_data("report_cards.json", report_cards)

    def view_all_letters(self):
        return list(load_data("letters.json").values())