from django.urls import path
from . import views

urlpatterns = [
    path('replenishment/', views.addtobalance, name='addtobalance')
]