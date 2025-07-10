from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import \
    gettext_lazy as _  # it let us translate the field into different anguages
from mentor_ship.mixins import DataTimeMixin

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin, DataTimeMixin):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site"),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


class Specialisation(models.Model, DataTimeMixin):
    name = models.CharField(max_length=100)

    def str(self):
        return f"{self.pk} - {self.name}"


class Teacher(models.Model, DataTimeMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    experience = models.IntegerField(verbose_name="experience in specialisation")
    specialisation = models.ForeignKey(
        Specialisation, on_delete=models.SET_DEFAULT, default="specialisation"
    )

    def str(self):
        return f"{self.pk} - user_id: {self.user}"

    class Meta:
        verbose_name = "teacher"
        verbose_name_plural = "teachers"


class Student(models.Model, DataTimeMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(
        max_digits=4, decimal_places=2
    )  # it is like float but it might not be negative

    def __str__(self):
        return f"{self.pk} - user_id: {self.user} - rating: {self.rating}"

    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"


class Group(models.Model, DataTimeMixin):
    name_of_the_group = models.CharField(max_length=100, blank=True)
    student = models.ManyToManyField(Student, blank=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, blank=True
    )
    course = models.ForeignKey(
        "testing_sistem.Course", on_delete=models.SET_NULL, null=True, blank=True
    )  # we can add connection with the model that is not exist yet \

    # with "name_of_the_application.Name_of_the_model", just in order \
    # we'll be able to make migrations
    def __str__(self):
        return f"{self.pk} - {self.name_of_the_group}"

    class Meta:
        verbose_name = "group"
        verbose_name_plural = "groups"
