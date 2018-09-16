from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^resume/$', views.ResumeView.as_view(), name='resume'),
    url(r'^projects/$', views.ProjectsView.as_view(), name='projects'),
    url(r'^contact/$', views.ContactFormView, name='contact'),
]

