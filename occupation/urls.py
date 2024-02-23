"""
Api end points for designation module
"""

from django.urls import path
from occupation import views

urlpatterns = [
    path('addNewOccupation/', views.addNewOccupation, name="addNewOccupation"),
    path('getAllOccupations/', views.getAllOccupations, name="getAllOccupations"), 
]