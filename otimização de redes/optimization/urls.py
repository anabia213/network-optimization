from django.urls import path
from . import views

urlpatterns = [
    path('network_data/', views.network_data, name='network_data'),
]
