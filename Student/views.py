from django.shortcuts import render

# Create your views here.

# views.py

from django.http import HttpResponse
from django.db import connection
from django.core.cache import cache

def test_db_connection(request):
    """
    Tests the connection to PostgreSQL RDS database by executing a simple query.
    """
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1;")
        row = cursor.fetchone()
    if row:
        return HttpResponse("PostgreSQL connection is working.")
    else:
        return HttpResponse("Failed to connect to PostgreSQL.")

def test_cache_connection(request):
    """
    Tests the connection to ElastiCache Redis by setting and getting a value.
    """
    # Set a value in cache
    cache.set('test_key', 'test_value', timeout=60)
    
    # Get the value from cache
    value = cache.get('test_key')
    
    if value == 'test_value':
        return HttpResponse("Redis connection is working.")
    else:
        return HttpResponse("Failed to connect to Redis.")
