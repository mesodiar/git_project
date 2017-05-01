from django.contrib import admin

from .models import Repo, Contributor

@admin.register(Repo)
class RepoAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ('username', 'commit_amount', 'repo')
