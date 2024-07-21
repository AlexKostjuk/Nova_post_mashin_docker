from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PostMachin(models.Model):
    adress = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.adress} {self.city}'

    def __repr__(self):
        return f'{self.adress} {self.city}'



class Locker(models.Model):
    size = models.ImageField()
    post_machin = models.ForeignKey(PostMachin, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.post_machin.adress} {self.post_machin.city} {self.pk} size= {self.size} status= {self.status}'

    def __repr__(self):
        return f'{self.post_machin.adress} {self.post_machin.city} {self.pk} size= {self.size} status= {self.status}'


