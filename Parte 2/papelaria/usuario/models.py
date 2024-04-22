from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    patrao = models.BooleanField(default=False, verbose_name='Patrão')