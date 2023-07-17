from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    number = models.IntegerField(max_length=30)

    def register(self):
        pass

    def auto(self):
        pass


class Company(models.Model):
    Name = models.CharField(max_length=30)
    spisok = models.CharField(max_length=30)


class House(models.Model):
    adress = models.CharField(max_length=30)
    col = models.CharField(max_length=30)
