# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('test_db_connection/', views.test_db_connection, name='test_db_connection'),
    path('test_cache_connection/', views.test_cache_connection, name='test_cache_connection'),
]
