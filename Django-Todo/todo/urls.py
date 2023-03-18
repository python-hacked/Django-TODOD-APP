
from .views import *
from django.urls import path


urlpatterns =[
   
    path('',index.as_view(),name="index"),
    path('<pk>/update',update.as_view(),name="update"),
    path('<pk>/delete',delete.as_view(),name="delete"),
]