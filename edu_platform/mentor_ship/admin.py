from django.contrib import admin

from .models import Group, Specialisation, Student, Teacher, User

admin.site.register(User)
admin.site.register(Specialisation)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Group)
