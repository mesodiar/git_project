from django.conf.urls  import url

from . import views

urlpatterns = [
    url(r'^$', views.get_url, name='get_url'),
    url(r'^repo/(?P<pk>\d+)/$',views.sync_repo, name='sync_repo'),
]
