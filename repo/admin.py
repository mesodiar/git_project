from django.contrib import admin

from .models import Repo, Contributor

myModels = [Repo, Contributor]
admin.site.register(myModels)
