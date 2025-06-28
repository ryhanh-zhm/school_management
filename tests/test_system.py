from models.admin import Admin
from models.teacher import Teacher
from models.vice_principal import VicePrincipal
from models.student import Student
from models.parent import Parent
from models.classroom import Classroom
from models.course import Course
from models.disciplinary import DisciplinaryRecord
from models.letter import Letter
from utils.data_manager import load_data, save_data
from utils.password_generator import generate_password
import string
import uuid

def test_system():
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

    # Test user IDs
    users = load_data("users.json")
    assert users[admin.id]["username"] == "Shahnaz Ghasemi", "Admin username incorrect"
    assert users[admin.id]["role"] == "admin", "Admin role incorrect"
    assert users[teacher.id]["username"] == "Sara Gooya", "Teacher username incorrect"
    assert users[teacher.id]["role"] == "teacher", "Teacher role incorrect"
    assert users[vp.id]["username"] == "Mahla Zare", "Vice Principal username incorrect"
    assert users[vp.id]["role"] == "vice_principal", "Vice Principal role incorrect"
    assert users[student.id]["username"] == "Reyhaneh Zahmatkesh", "Student username incorrect"
    assert users[student.id]["role"] == "student", "Student role incorrect"
    assert users[parent.id]["username"] == "Alireza Zahmatkesh", "Parent username incorrect"
    assert users[parent.id]["role"] == "parent", "Parent role incorrect"

    # Create classroom
    classroom = Classroom("class1")
    classroom._save()

    # Assign student to classroom
    classroom.add_student(student.id)
    students = load_data("students.json")
    student_data = students[student.id]
    assert student_data["classroom_id"] == "class1", "Student not assigned to classroom"
    assert student.id in classroom.students, "Student not added to classroom"

    # Create course
    course = Course("course1", "Math")
    course._save()
    teacher.courses.append(course.id)
    teacher._save()
    classroom.add_course(course.id, teacher.id, "Monday 8:00")

    # Add grade
    teacher.add_grade(student.id, course.id, "term1", 15, 10, 12, 18)
    students = load_data("students.json")
    student_data = students[student.id]
    assert student_data["grades"][course.id]["term1"]["total"] == (15 + 10 + 12) * 1 + 18 * 2, "Grade calculation incorrect"

    # Add disciplinary record
    record = DisciplinaryRecord("absence", "Unexcused absence")
    record._save()
    student.add_disciplinary_record(record.id)
    disciplinary_records = load_data("disciplinary.json")
    assert record.id in disciplinary_records, "Disciplinary record not saved"
    assert len(student.disciplinary_records) == 1, "Disciplinary record not added"

    # Send letter
    letter = Letter(student.id, teacher.id, "Hello, I have a question?")
    letter._save()
    letters = load_data("letters.json")
    assert letter.id in letters, "Letter not saved"
    assert letters[letter.id]["sender_id"] == student.id, "Sender ID incorrect"
    assert letters[letter.id]["receiver_id"] == teacher.id, "Receiver ID incorrect"
    assert len(admin.view_all_letters()) == 1, "Letter not visible to admin"

    # Test invalid letter sending
    try:
        Letter("invalid_id", teacher.id, "Invalid letter")
        assert False, "Should raise ValueError for invalid sender ID"
    except ValueError as e:
        assert str(e).startswith("Sender ID"), "Expected sender ID error"

    # Test report card
    admin.issue_report_cards("term1")
    report_cards = load_data("report_cards.json")
    assert f"{student.id}_term1" in report_cards, "Report card not generated"

    # Test password generator
    test_password_generator()
    print("All tests passed!")

def test_password_generator():
    password = generate_password()
    assert len(password) == 8, "Password length should be 8"
    assert all(c in (string.ascii_letters + string.digits) for c in password), "Password should only contain letters and digits"
    print("Password generator test passed!")

if __name__ == "__main__":
    test_system()