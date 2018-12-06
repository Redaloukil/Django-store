from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=length, ${blank=True, null=True}) 
    description = models.TextField(_(""))
    
class Image(models.Model):
    product = models.ForeignKey(Product, related_name='', on_delete=models.CASCADE)
    image = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
)