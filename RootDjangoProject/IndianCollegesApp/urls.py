from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('states/<int:state_id>/', views.state),
]