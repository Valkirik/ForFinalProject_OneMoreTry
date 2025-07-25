from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .consts import USER_DATA, create_user
from .serializer import StudentSerializer, TeacherSerializer, UserSerializer


class CreateUserTest(APITestCase):
    def test_create_user(self):
        url = reverse("user-list")
        response = self.client.post(url, data=USER_DATA, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadUserTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_read_user_list(self):
        url = reverse("user-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_user_detail(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateUserTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.data = UserSerializer(self.user).data
        self.data.update({"first_name": "new_Test_fn"})

    def test_update_user(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteUserTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_delete_user(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.specialization = create_specialization()

    def test_create_teacher(self):
        url = reverse("teacher-list")
        response = self.client.post(url, data={"experience": 10, "user": self.user.id, "specialization": [self.specialization.id]}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.specialization = create_specialization()
        self.teacher = create_teacher(self.user, self.specialization)

    def test_read_teacher_list(self):
        url = reverse("teacher-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_teacher_detail(self):
        url = reverse("teacher-detail", args=[self.teacher.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTeacherTest(APITestCase):
    def setUp(self):
        self.teacher = create_teacher(user=create_user(), specialization=create_specialization())
        self.data = TeacherSerializer(self.teacher).data
        self.data.update({"experience": 15})

    def test_update_teacher(self):
        url = reverse("teacher-detail", args=[self.teacher.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteTeacherTest(APITestCase):
    def setUp(self):
        self.teacher = create_teacher(user=create_user(), specialization=create_specialization())

    def test_delete_teacher(self):
        url = reverse("teacher-detail", args=[self.teacher.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateStudentTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_create_student(self):
        url = reverse("student-list")
        response = self.client.post(url, data={"rating": 10.0, "user": self.user.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadStudentTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)

    def test_read_student_list(self):
        url = reverse("student-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_student_detail(self):
        url = reverse("student-detail", args=[self.student.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateStudentTest(APITestCase):
    def setUp(self):
        self.student = create_student(user=create_user())
        self.data = StudentSerializer(self.student).data
        self.data.update({"rating": 10.1})

    def test_update_student(self):
        url = reverse("student-detail", args=[self.student.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteStudentTest(APITestCase):
    def setUp(self):
        self.student = create_student(user=create_user())

    def test_delete_student(self):
        url = reverse("student-detail", args=[self.student.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateGroupTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)
        self.specialization = create_specialization()
        self.teacher = create_teacher(self.user, self.specialization)
        self.course = create_course(self.teacher, self.specialization)

    def test_create_group(self):
        url = reverse("group-list")
        response = self.client.post(url, data={"student": [self.student.id], "teacher": self.teacher.id, "course": self.course.id, "title": "Веб"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
