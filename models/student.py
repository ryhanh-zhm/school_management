from models.user import User
from utils.data_manager import load_data, save_data

class Student(User):
    def __init__(self, username, parent_username):
        super().__init__(username, "student")
        self.classroom_id = None
        self.grades = {}
        self.disciplinary_records = []
        self.parent_username = parent_username
    
    def assign_classroom(self, classroom_id):
        if self.classroom_id:
            raise ValueError("Student already assigned to a classroom!")
        self.classroom_id = classroom_id
        self._save()
    
    def add_grade(self, course_id, term, midterm, activity, quiz, final):
        if course_id not in self.grades:
            self.grades[course_id] = {}
        self.grades[course_id][term] = {
            "midterm" : midterm, 
            "activity" : activity, 
            "quiz" : quiz, 
            "final" : final, 
            "total" : (midterm + activity + quiz) * 1 + final * 2
        } 
        self._save()
    
    def add_disciplinary_record(self, record):
        self.disciplinary_records.append(record)
        self._save()

    def view_dashboard(self):
        return {
            "grades" : self.grades, 
            "disciplinary_records": self.disciplinary_records
        }
    
    def _save(self):
        students = load_data("student.json")
        students[self.id] = self.__dict__
        save_data("student.json", students)
