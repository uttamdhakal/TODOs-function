from django.conf.urls import url
from . import views

app_name = 'tracker'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    #add
    url(r'todo/add/$', views.AlbumCreate.as_view(), name = 'todo-add'),

]


