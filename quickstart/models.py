from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	user = models.ForeignKey(User, unique=True)
	direccion = models.CharField(max_length=250, blank=True)
	telefono = models.PositiveIntegerField(null=True, blank=True)
