import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def nickname(self):
        return f'{self.first_name}_{self.last_name}'.lower()


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    mobile = models.CharField(max_length=10, null=True,
                              blank=True)  # todo: convert to phone-field
    mobile_confirmed = models.BooleanField(default=False)
    national_id = models.IntegerField(default=None, null=True, blank=True)
    national_id_confirmed = models.BooleanField(default=False)
    medical_id = models.IntegerField(default=None, null=True, blank=True)
    medical_id_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
