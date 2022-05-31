from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createuniversity', views.createuniversity),
    path('alluniversity', views.alluniversity),
    path('create', views.create),
    path('all', views.all),
    path('update',views.update),
    path('delete',views.delete),
]