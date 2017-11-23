from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^personas/$', views.PersonaList.as_view()),
    url(r'^persona/(?P<nickname>[a-zA-Z0-9]+)/$', views.PersonaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
