from django.urls import path
from .views import manage_students

urlpatterns = [
    path('', manage_students, name='manage_students'),
]
