from django.db import models

class Repo(models.Model):
    name = models.CharField(
        max_length=200
    )
    owner = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name

class Contributor(models.Model):
    username =  models.CharField(
        max_length=100
    )
    commit_amount = models.CharField(
        max_length=50
    )
    repo = models.ForeignKey(
        Repo
    )

    def __str__(self):
        return self.username
