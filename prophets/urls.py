from django.urls import path, include
from rest_framework.routers import DefaultRouter

from prophets import views

router = DefaultRouter()
router.register(r'prophet', views.ProphetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]