from rest_framework import permissions, viewsets
from .models import Answer, Article, Course, Image, Questions, Test, Topic
from .serializer import AnswerSerializer, ArticleSerializer, CourseSerializer, ImageSerializer, \
    QuestionsSerializer, TestSerializer, TopicSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.AllowAny]

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]

class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    permission_classes = [permissions.AllowAny]

class TestViewSet(viewsets.ModelViewSet):
    queryset =Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.AllowAny]

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.AllowAny]