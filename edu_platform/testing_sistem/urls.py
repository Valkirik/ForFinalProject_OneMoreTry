from django.urls import include, path, re_path
from rest_framework import routers

from .endpoints import (AnswerViewSet, ArticleViewSet,
                        CourseListSpecialisationAPIview, CourseViewSet,
                        QuestionsViewSet, TestViewSet, TopicViewSet)

router = routers.SimpleRouter()
router.register("answer_viewset", AnswerViewSet),
router.register("article_vieset", ArticleViewSet),
router.register("course_viewset", CourseViewSet),
router.register("question_viewset", QuestionsViewSet),
router.register("test_viewset", TestViewSet),
router.register("topic_register", TopicViewSet),

urlpatterns = [
    path("", include(router.urls)),
    re_path(
        "specialisation/(?P<id>.+)/course_list",
        CourseListSpecialisationAPIview.as_view(),
    ),
]
