from rest_framework.serializers import ModelSerializer
from .models import User, Specialisation, Teacher, Student, Group

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class SpecialisationSerializer(ModelSerializer):
    class Meta:
        model = Specialisation
        fields = "__all__"

class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class GroupStudentSerializer(ModelSerializer):
    class Meta:
        model = Group

    def to_representation(self, object):
        if isinstance(object, Group):
            serializer = GroupSerializer(object)
        elif isinstance(object, Student):
            serializer = StudentSerializer(object)
        else:
            raise Exception("There is nothing to serialize. Select or the group ether the student")
        return serializer.data
