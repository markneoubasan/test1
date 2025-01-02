from django.db import models
from django.urls import reverse


class Post(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'pk': self.pk})

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    verified_credentials = models.BooleanField(default=False)
    years_of_experience = models.IntegerField()
    profile_picture = models.ImageField(upload_to='instructors/', blank=True, null=True)
    specialties = models.CharField(max_length=200)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('team_detail', kwargs={'pk': self.pk})
