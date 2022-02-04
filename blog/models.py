from django.db import models

# Create your models here.

class User(models.Model):
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    class Meta:
        db_table='blog_db'


class Post(models.Model):
    text = models.CharField(max_length=1000)
    created_at = models.DateField()
    updated_at = models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='useref')
    class Meta:
        db_table='post_master'