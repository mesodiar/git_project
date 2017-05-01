from django.shortcuts import render

import requests

def repo_home(request):
    return render(request, 'templates/home.html', {})
