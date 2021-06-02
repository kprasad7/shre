from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

from vendor.models import Vendor

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    employes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Product(models.Model):
    company_name = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    other_costs = models.DecimalField(max_digits=6, decimal_places=2)
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, related_name='services', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='services', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    project_cost = models.DecimalField(max_digits=6, decimal_places=0)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    
    def __str__(self):
        return self.company_name
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/120x120.jpg'
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail