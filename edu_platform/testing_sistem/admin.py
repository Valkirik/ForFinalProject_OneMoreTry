from django.contrib import admin

from .models import Answer, Article, Course, Questions, Test, Topic

admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Article)
admin.site.register(Test)
admin.site.register(Questions)
admin.site.register(Answer)
