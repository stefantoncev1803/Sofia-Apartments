from django.db import models


class User(models.Model):

    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password1 = models.CharField(max_length = 100)
    password2 = models.CharField(max_length = 100)
    def __str__(self):
        return self.username


class Apartments(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.TextField()
    type = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    district = models.CharField(max_length = 100)
    price = models.FloatField()
    size = models.IntegerField()
    floor = models.IntegerField()
    images = models.ImageField(upload_to ='static/rent_website/images')
    favorite = models.BooleanField()
    def __str__(self):
        return self.type + "-"+ self.city



