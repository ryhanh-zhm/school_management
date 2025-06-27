from utils.data_manager import load_data, save_data

class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name
    
    def _save(self):
        courses = load_data("courses.json")
        courses[self.id] = self.__dict__
        save_data("courses.json", courses)