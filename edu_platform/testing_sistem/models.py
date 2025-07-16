from django.db import models
from mentor_ship.models import DataTimeMixin, Specialisation, Teacher


class Image(models.Model):
    image = models.ImageField(null=True, blank=True)


class Course(models.Model, DataTimeMixin):
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, blank=True
    )
    specialisation = models.ManyToManyField(Specialisation, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"


class Topic(models.Model, DataTimeMixin):
    title = models.CharField(max_length=100)
    description = models.TimeField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    index_number = models.IntegerField()
    image = models.ManyToManyField(Image, blank=True, null=True)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "topic"
        verbose_name_plural = "topics"


class Article(models.Model, DataTimeMixin):
    title = models.CharField(max_length=100)
    topic_id = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    content = models.FileField(null=True, blank=True)
    author = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"


class Test(models.Model, DataTimeMixin):
    title = models.CharField(max_length=100)
    description = models.TimeField()
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    is_open = models.BooleanField(default=False)

    def __str__(self):
        def __str__(self):
            return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "test"
        verbose_name_plural = "tests"


class Questions(models.Model, DataTimeMixin):
    content = models.CharField(max_length=100)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} - {self.content}"

    class Meta:
        verbose_name = "question"
        verbose_name_plural = "questions"


class Answer(models.Model, DataTimeMixin):
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} - {self.text}"

    class Meta:
        verbose_name = "answer"
        verbose_name_plural = "answers"
