from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from .models import User, Specialisation, Student, Teacher, Group
from .serializer import UserSerializer, SpecialisationSerializer, StudentSerializer, TeacherSerializer, GroupSerializer, GroupStudentSerializer
from itertools import chain

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class SpecialisationViewSet(viewsets.ModelViewSet):
    queryset = Specialisation.objects.all()
    serializer_class = SpecialisationSerializer
    permissions = [permissions.AllowAny]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permissions = [permissions.AllowAny]

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permissions = [permissions.AllowAny]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permissions = [permissions.AllowAny]


#here we get the list with the group and the students of these group

class AllGroupStudentListAPIview(ListAPIView):
    serializer_class = GroupStudentSerializer
    permissions = [permissions.AllowAny]
    def get_queryset(self):
        group_queryset = Group.objects.all()
        student_queryset = Student.objects.all()
        queryset = chain(set(group_queryset), set(student_queryset))
        return queryset


#here we get all the students from the certain group

class StudentsGroupListAPIview(ListAPIView):
    serializer_class = StudentSerializer
    permissions = [permissions.AllowAny]
    def get_queryset(self):
        group_id = self.kwargs["id"]
        student_queryset = Student.objects.all()
        return student_queryset

