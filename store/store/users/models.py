from django.contrib.auth.models import AbstractUser 
from django.db.models import CharField 
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    phone_number = CharField(_(""),max_length=255)
    
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return self.username
    