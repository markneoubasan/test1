from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Admin(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default='')
    body = models.TextField()

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'pk': self.pk})


class Course(models.Model):
    course_type = models.CharField(max_length=100, default='')
    description = models.TextField()
    duration = models.CharField(max_length=100)
    instructor = models.ForeignKey('Instructor', on_delete=models.SET_NULL, null=True, related_name='courses')

    def __str__(self):
        return f"{self.course_type}"

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'pk': self.pk})


class Enrollment(models.Model):
    COURSE_TYPES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Disapproved', 'Disapproved')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField()
    enrollment_status = models.CharField(max_length=11, choices=COURSE_TYPES, default='Pending')

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.course_type}"

    def get_course(self):
        return self.course


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    verified_credentials = models.ImageField(upload_to='media/credentials', blank=True, null=True)
    years_of_experience = models.CharField(max_length=100, default='')
    profile_picture = models.ImageField(upload_to='media/instructors', blank=True, null=True)
    specialties = models.CharField(max_length=200)
    contact_email = models.EmailField()
    phone_number = models.IntegerField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('team_detail', kwargs={'pk': self.pk})

