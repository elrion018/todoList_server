from django.urls import path
from . import views
urlpatterns = [
    path('signup', views.signUp),
    path('signin', views.signIn)

]
