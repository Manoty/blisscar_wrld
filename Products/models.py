from django.db import models
from PIL import Image
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)
    transmission = models.CharField( max_length=100, blank=False, null=False)
    mileage= models.IntegerField(default=0, null=True, blank=False,)
    image = models.ImageField(upload_to='static/images/Products/')
    price = models.IntegerField(blank=False, null=False)



    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        img = Image.open(self.image.path)


        if img.height < 462 or img.width < 340:
            output_size = (462, 340)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.name


