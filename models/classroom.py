# models/classroom.py
from utils.data_manager import load_data, save_data
from models.student import Student
import time
import os
import json

class Classroom:
    def __init__(self, class_id):
        self.id = class_id
        self.students = []
        self.courses = []

    def add_student(self, student_id):
        students = load_data("students.json")
        student_data = students.get(student_id)
        if not student_data:
            # Retry loading in case of timing or file handle issue
            time.sleep(0.2)  # Delay to ensure file write completes
            # Force reload by re-reading the file
            file_path = os.path.join("data", "students.json")
            with open(file_path, 'r') as f:
                content = f.read().strip()
                if content:
                    f.seek(0)  # Reset pointer to start before loading
                    students = json.load(f)
                else:
                    students = {}
            student_data = students.get(student_id)
            if not student_data:
                raise ValueError("Student not found")
        if student_data.get("classroom_id"):
            raise ValueError("Student already in a class")
        self.students.append(student_id)
        student_obj = Student(student_data["username"], student_data["parent_username"])
        student_obj.id = student_data["id"]
        student_obj.classroom_id = student_data.get("classroom_id")
        student_obj.grades = student_data.get("grades", {})
        student_obj.disciplinary_records = student_data.get("disciplinary_records", [])
        student_obj.assign_classroom(self.id)
        self._save()

    def add_course(self, course_id, teacher_id, schedule):
        classrooms = load_data("classrooms.json")
        for cls in classrooms.values():
            for c in cls["courses"]:
                if c["schedule"] == schedule and cls["id"] != self.id:
                    raise ValueError("Schedule conflict")
        self.courses.append({"course_id": course_id, "teacher_id": teacher_id, "schedule": schedule})
        self._save()

    def _save(self):
        classrooms = load_data("classrooms.json")
        classrooms[self.id] = self.__dict__
        save_data("classrooms.json", classrooms)