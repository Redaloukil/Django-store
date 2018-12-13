from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Category(models.Model):
    title = models.CharField(_("") , max_length=255, blank=True, null=True)
    description = models.CharField(_("") ,max_length=255 ,blank=True, null=True)
    

class Product(models.Model):
    title = models.CharField(_("") , max_length=200, blank=False, null=True) 
    description = models.TextField(_(""))
    category = models.ForeignKey(Category, verbose_name=_(""), on_delete=models.CASCADE)
    price = models.CharField(max_length=100,)

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Image(models.Model):
    product = models.ForeignKey(Product, related_name='Product', on_delete=models.CASCADE)
    image = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class Sale(models.Model):
    Product = models.OneToOneField(Product, verbose_name=_(""), on_delete=models.CASCADE)