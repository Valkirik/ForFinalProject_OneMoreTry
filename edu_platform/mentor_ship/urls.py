from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework.routers import SimpleRouter
from .endpoints import UserViewSet, SpecialisationViewSet, StudentViewSet, TeacherViewSet, \
    GroupViewSet, AllGroupStudentListAPIview, StudentsGroupListAPIview

router = routers.SimpleRouter()
router.register('user_viewset', UserViewSet)
router.register('specialisation_viewset', SpecialisationViewSet)
router.register('student_viewset', StudentViewSet)
router.register('teacher_viewset', TeacherViewSet)
router.register('group_viewset', GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("group_student/", AllGroupStudentListAPIview.as_view()),
    re_path("group/(?P<id>.+)/student_list", StudentsGroupListAPIview.as_view()),

]