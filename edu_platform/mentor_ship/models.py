from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import \
    gettext_lazy as _  # it let us translate the field into different anguages
from .managers import CustomUserManager


class DataTimeMixin:
    data_created = models.DateTimeField(auto_now=True)
    data_updated = models.DateTimeField(auto_now=True)


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

    objects = CustomUserManager()  # to write a class CustomUserManager

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


"""class Student(models.Model, DataTimeMixin):
    pass


class Teacher(models.Model, DataTimeMixin):
    pass
"""