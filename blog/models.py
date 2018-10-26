# from django.db import models
from django.utils import timezone
from djongo import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    nama = models.CharField(max_length=100)
    harga= models.IntegerField()
    pengarang = models.CharField(max_length=100)
    penerbit = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nama
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})


