from django.db import models

# Create your models here.
from django.db import models


class Netflix(models.Model):
    """
    Netflix Model
    Defines the attributes of the Netflix database
    """
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    country = models.CharField(max_length=255)
    country_code=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_country(self):
        return self.name + ' belongs to ' + self.country + ' country.'

    def __repr__(self):
        return self.name + ' is added.'

class Payment(models.Model):
    payment_id=models.IntegerField()
    creditcard = models.IntegerField()

class contact(models.Model):
    phone = models.IntegerField(max_length=10)
    address = models.CharField(max_length=255)

class Movies(models.Model):
    currentmovie = models.CharField(max_length=255)
    Watched = models.Charfield(max_length=1056)
    Recommended = models.Charfield(max_length=1056)

class Genre(models.Model):
    genre_id = models.IntegerField()
    genre = models.Charfield(max_length=256)

class FAQ(models.Model):
    Most_asked = models.CharField(max_length=256)
    Important questions = models.Charfield(max_length=256)

class waystowatch(models.Model):
    Mobile = models.CharField()
    StoreApplication = models.Charfield(max_length=256)

class Shows(models.Model):
    show_no = models.IntegerField()
    show_name = models.Charfield(max_length=256)

class Customer(models.Model):
    customer_id = models.IntegerField()
    customer_subscription = models.Charfield(max_length=256)
