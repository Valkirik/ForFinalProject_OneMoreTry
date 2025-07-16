from rest_framework.serializers import ModelSerializer

from .models import Answer, Article, Course, Image, Questions, Test, Topic


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class QuestionsSerializer(ModelSerializer):
    class Meta:
        model = Questions
        fields = "__all__"


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


# with image it does not work (just to see the error)
class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class TopicArticlesSerializer(ModelSerializer):
    class Meta:
        model = Topic

    def to_representation(self, object):
        match isinstance(object, Topic):
            case True:
                serializer = TopicSerializer(object)
            case False:
                serializer = ArticleSerializer(object)
            case _:
                raise Exception(
                    "There is nothing to serialize. Select or the group ether the student"
                )
        return serializer.data
