from home.views import index, person_view
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('Person', person_view, name='Person')
]
