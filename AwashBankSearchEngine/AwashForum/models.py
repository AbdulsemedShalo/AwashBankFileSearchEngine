
# Models are the layouts for Database

from django.db import models
# For User Model there is no need of creating models
# We can simple use built in DJango User by importing from django.contrib.auth.models import User

from django.contrib.auth.models import User 

# Create your models here.

# Created as Board Table in the database
class Board(models.Model):
    name = models.CharField(max_length=30, unique = True)
    description = models.TextField(max_length = 100)
    
    def __str__(self):
        return self.name
    

# Created as Topic table in the database
class Topic(models.Model):
    subject = models.CharField(max_length = 255)
    board = models.ForeignKey(Board, on_delete = models.CASCADE, related_name ='topics')
    starter = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'topics')
    last_updated = models.DateTimeField()
    
    def __str__(self) :
        return self.subject
    
# Created as Post Table in the database
class Post(models.Model):
    message = models.TextField(max_length = 5000)
    topics =  models.ForeignKey(Topic, on_delete = models.CASCADE, related_name = 'posts')
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'posts')
    updated_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name = '+')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at =  models.DateTimeField(null = True)
    
    def __str__(self):
        return self.message
 