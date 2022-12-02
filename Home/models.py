from django.db import models


class Contact(models.Model):
    SNo = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    SNo = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=100)
    ImageUrl = models.CharField(max_length=100)
    ProjectDescription = models.TextField()
    SourceCode = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.ProjectName