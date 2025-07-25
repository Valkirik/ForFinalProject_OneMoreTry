from testing_system.models import Course

from .annotations import (
    SpecializationAnnotation,
    StudentAnnotation,
    TeacherAnnotation,
    UserAnnotation,
)
from .models import Group, Specialization, Student, Teacher, User

USER_DATA = {"password": "qwerty", "first_name": "Test_fn", "last_name": "Test_sn", "email": "test1@email.com"}


def create_user() -> UserAnnotation:
    user = User.objects.create_user(password="qwerty", first_name="Test_fn", last_name="Test_sn", email="test@email.com")
    return user


def create_teacher(user: UserAnnotation, specialization: SpecializationAnnotation) -> TeacherAnnotation:
    teacher = Teacher.objects.create(experience=10, user=user)
    teacher.specialization.add(specialization.id)
    return teacher


def create_specialization() -> SpecializationAnnotation:
    specialization = Specialization.objects.create(title="Test_spec")
    return specialization


def create_student(
    user: UserAnnotation,
) -> StudentAnnotation:
    student = Student.objects.create(rating=10.0, user=user)
    return student


def create_group(teacher: TeacherAnnotation, student: StudentAnnotation, course):
    group = Group.objects.create(title="Python1", teacher=teacher, student=student, course=course)
    return group


def create_course(teacher: TeacherAnnotation, specialization: SpecializationAnnotation):
    course = Course.objects.create(title="Python", teacher=teacher, description="Вебразработка")
    course.specialization.add(specialization.id)
    return course