from django.urls import path # type: ignore
from .views import django_logo

urlpatterns = [
    path('logo/', django_logo, name='django_logo'),
]

from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]
