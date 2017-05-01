from django.db import models

class Repo(models.Model):
    name = models.CharField(
        max_length=200
    )
    url = models.CharField(
        max_length=300
    )

    def __str__(self):
        return self.name

class User(models.Model):
    username =  models.CharField(
        max_length=200
    )
    commit_amount = models.IntegerField()
    repo = models.ForeignKey(
        Repo
    )

    def __str__(self):
        return self.username
