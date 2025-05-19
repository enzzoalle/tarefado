from django.db import models
import random
import string
from django.contrib.auth.models import User

def gerador_randomico_code():
     caracteres = string.ascii_letters + string.digits
     return ''.join(random.choices(caracteres, k=8))

class CodigoEmail(models.Model):
     code = models.CharField(max_length=8, unique=True, default=gerador_randomico_code)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     data_code = models.DateTimeField(auto_now_add=True)