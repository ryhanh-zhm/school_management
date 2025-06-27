from models.admin import Admin
from models.teacher import Teacher
from models.student import Student
from models.parent import Parent
from models.classroom import Classroom
from models.course import Course
from models.disciplinary import DisciplinaryRecord
from models.letter import Letter
from models.vice_principal import VicePrincipal
import random

def main():
    # Initialize admin
    admin = Admin("Shahnaz Ghasemi")
    admin._save()

    # Add teacher
    teacher = admin.add_teacher("Sara Gooya")
    teacher._save()

    # Add vice principal
    vp = admin.add_vice_principal("Mahla Zare")
    vp._save()

    # Add student and parent
    student = Student("Reyhaneh Zahmatkesh", "Alireza Zahmatkesh")
    student._save()
    parent = Parent("Alireza Zahmatkesh", student.id)
    parent._save()

    # Create classroom
    classroom = Classroom("class1")
    classroom._save()

    # Assign student to classroom
    classroom.add_student(student.id)

    # Create course
    course = Course("course1", "Math")
    course._save()
    teacher.courses.append(course.id)  # Added to assign course to teacher
    teacher._save()  # Save updated teacher
    classroom.add_course(course.id, teacher.id, "Monday 8:00")

    # Add grade
    teacher.add_grade(student.id, course.id, "term1", 15, 10, 12, 18)

    # Add disciplinary record
    record = DisciplinaryRecord("absence", "Unexcused absence")
    record._save()
    student.add_disciplinary_record(record.id)

    # Send letter
    letter = Letter(student.id, teacher.id, "Hello, I have a question?")
    letter._save()

    # View student dashboard
    print(student.view_dashboard())

    # View parent dashboard
    print(parent.view_student_dashboard())

    # View teacher classes
    print(teacher.view_classes())

    # Issue report card
    admin.issue_report_cards("term1")

if __name__ == "__main__":
    main()