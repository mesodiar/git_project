from django.conf.urls  import url

from . import views

urlpatterns = [
    url(r'^$', views.repo_home, name='repo_home'),
]
