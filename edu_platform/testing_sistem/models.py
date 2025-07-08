from django.db import models
from mentor_ship.models import DataTimeMixin, Teacher


class Course(models.Model, DataTimeMixin):
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, blank=True
    )
    description = models.TimeField

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"
