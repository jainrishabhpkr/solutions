from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, pre_save

from solutions.utils import unique_slug_generator
# Create your models here.



class Product(models.Model):
    PRODUCT_CHOICES = (('clothes','Clothes'),('appliances','Appliances'),('furniture','Furniture'))
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=256)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    categories = models.CharField(max_length=10, choices = PRODUCT_CHOICES )

    def get_absolute_url(self):

        return reverse("product-detail" , kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver,  sender=Product)
