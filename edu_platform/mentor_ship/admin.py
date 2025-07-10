from django.contrib import admin

from .models import User, Specialisation, Teacher, Student

admin.site.register(User)
admin.site.register(Specialisation)
admin.site.register(Teacher)
admin.site.register(Student)
"""admin.site.register(Group)"""

