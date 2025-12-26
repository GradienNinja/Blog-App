from django.urls import path 
from . views import * 


urlpatterns = [
  path('',home,name="home"),
  path('create/',create_post,name="create"),
  path('edit/<int:id>/',edit_post,name="edit")
]
