from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import URLForm
from .models import Contributor, Repo

import requests

def get_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            input_url = form.cleaned_data['input_url']
            split_url = input_url.split('/')
            api_url = f'https://api.github.com/repos/{split_url[3]}/{split_url[4]}/contributors'
            repo, created = Repo.objects.get_or_create(
                name=split_url[4],
                owner=split_url[3]
            )
            data = requests.get(api_url)
            for account in data.json():
                username = account.get("login")
                commits = account.get("contributions")

                contributor, created = Contributor.objects.get_or_create(
                    username = username,
                    commit_amount = commits,
                    repo = repo
                )

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = URLForm()
        repo_names = Repo.objects.all()
        contributors = Contributor.objects.values('repo', 'username', 'commit_amount')
        print(contributors)
        return render(request, 'templates/home.html', {
            'form': form,
            'repo_names': repo_names,
            'contributors': contributors
            }
        )
