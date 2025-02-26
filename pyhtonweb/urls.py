from django.urls import path

from pyhtonweb import views

urlpatterns = [
    path('/',views.home, name='home' ),
]
