from django.db import models

# Create your models here.


class Students(models.Model):
    studentid = models.CharField(max_length=10, primary_key=True)
    nomonjersey = models.CharField(max_length=100)
    studentname = models.TextField()
    semester = models.IntegerField()
    phonenumber = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)


class Lecturers(models.Model):
    lecturerid = models.CharField(max_length=10, primary_key=True)
    lecturername = models.TextField()
    lecturernumber = models.CharField(max_length=20)
    lectureremail = models.CharField(max_length=50)
    lecturerpasword = models.CharField(max_length=20)


class Meetups(models.Model):
    M_title = models.CharField(max_length=100)
    M_description = models.TextField()
    M_date = models.DateField()
    M_time = models.TimeField()
    M_location = models.TextField()


class Tournament(models.Model):
    tittle = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=50)
