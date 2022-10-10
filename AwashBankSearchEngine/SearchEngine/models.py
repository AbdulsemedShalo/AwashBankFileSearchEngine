from django.db import models

# Create your models here.

#a model class to upload our file or document into our database
class FileAndDocumentBase(models.Model):
    fileCategory=models.CharField(max_length=100)
    fileContent=models.FileField()
    publicaitonDate=models.DateTimeField("PublicationDate")
    publishedBy=models.CharField(max_length=100)

    def _str_(self):
        return self.fileContent

# a model class to create system admins profile base to perform CRUD operations
class systemAdministrators(models.Model):
    firstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Role=models.CharField(max_length=100)
    jobPosition=models.CharField(max_length=100)
    profilePicture=models.FileField()
    userName=models.CharField(max_length=100)
    PassWord=models.CharField(max_length=100)
    publicaitonDate=models.DateTimeField("PublicationDate")
    publishedBy=models.CharField(max_length=100)

    def _str_(self):
        return self.firstName

#a notificaiton post by admin for the system users
class Announcements(models.Model):
    Title=models.CharField(max_length=100)
    MessageContent=models.TextField()
    publicaitonDate=models.DateTimeField("PublicationDate")
    publishedBy=models.CharField(max_length=100)

    def _str_(self):
        return self.MessageContent


# a model for creating the categories under which files and documents are indexed
class Category(models.Model):
    categoryTitle=models.CharField(max_length=100)
    publicationDate=models.DateTimeField()

    def _str_(self):
        return self.categoryTitle
    


#a model creation for the discussion panel where users can raise or create a post that is shared and answered by the admin
class discussionBoard(models.Model):
    boardMessage=models.TextField()
    publicaitonDate=models.DateTimeField("PublicationDate")
    publishedBy=models.CharField(max_length=100)

    def _str_(self):
        return self.boardMessage


