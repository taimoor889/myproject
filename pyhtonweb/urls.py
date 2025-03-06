from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import projectviewset

router = DefaultRouter()
router.register(r'project', projectviewset, basename='project')

urlpatterns = [
    path('', include(router.urls)),  # This will include the URLs registered by the router
]
