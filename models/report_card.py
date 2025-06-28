from utils.data_manager import load_data, save_data

class ReportCard:
    def __init__(self, student_id, term):
        self.student_id = student_id
        self.term = term
        students = load_data("students.json")
        self.grades = students.get(self.student_id, {}).get("grades", {})

    def _save(self):
        report_cards = load_data("report_cards.json")
        report_cards[f"{self.student_id}_{self.term}"] = self.__dict__
        save_data("report_cards.json", report_cards)