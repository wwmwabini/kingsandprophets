from django.urls import path
from kings import views

urlpatterns = [
    path('get_all_kings/', views.get_all_kings, name='get-all-kings'),
]