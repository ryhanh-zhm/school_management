from utils.data_manager import load_data, save_data

class ReportCard:
    def __init__(self, student_id, term):
        self.student_id = student_id
        self.term = term
        self.grades = {}
        self.disciplinary_score = 20  # Default
        self.disciplinary_records = []

    def generate(self):
        students = load_data("students.json")
        student = students.get(self.student_id)
        if not student:
            raise ValueError("Student not found")
        self.grades = student["grades"]
        self.disciplinary_records = student["disciplinary_records"]
        self.disciplinary_score -= len(self.disciplinary_records) * 2  # Deduct 2 points per record
        self._save()

    def _save(self):
        report_cards = load_data("report_cards.json")
        report_cards[f"{self.student_id}_{self.term}"] = self.__dict__
        save_data("report_cards.json", report_cards)