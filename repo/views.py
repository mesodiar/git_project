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
            print(api_url)
            repo, created = Repo.objects.get_or_create(
                name=split_url[3],
                owner=split_url[4]
            )
            data = requests.get(api_url)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = URLForm()
        repo_names = Repo.objects.all()
        return render(request, 'templates/home.html', {'form': form, 'repo_names': repo_names})
