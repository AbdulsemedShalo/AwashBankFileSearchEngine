from django.db import models

# Create your models here.

#a model class to upload our file or document into our database
class FileAndDocumentBase(models.Model):
    fileCategory=models.CharField(max_length=100)
    fileContent=models.FileField()
    publicaitonDate=models.DateTimeField("Publication Date")
    publishedBy=models.CharField(max_length=100)

    def _str_(self):
        return self.fileContent

# a model for creating the categories under which files and documents are indexed
class Category(models.Model):
    categoryTitle=models.ForeignKey(FileAndDocumentBase, on_delete = models.CASCADE, related_name = 'categories')
    publicationDate=models.DateTimeField()

    def _str_(self):
        return self.categoryTitle
    


