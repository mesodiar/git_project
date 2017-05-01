from django.shortcuts import render

from .forms import URLForm

import requests

def get_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            input_url = form.cleaned_data['input_url']
            split_url = input_url.split('/')
            api_url = f'https://api.github.com/repos/{split_url[3]}/{split_url[4]}/contributors'
            print(api_url)
            repo = requests.get(api_url)
    else:
        form = URLForm()
    return render(request, 'templates/home.html', {'form': form})
