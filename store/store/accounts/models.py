from django.db import models
from users.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, verbose_name=_(""), on_delete=models.CASCADE)
    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class Provider(models.Model):
    user = models.OneToOneField(User, verbose_name=_(""), on_delete=models.CASCADE)