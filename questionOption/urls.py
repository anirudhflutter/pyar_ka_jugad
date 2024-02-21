"""
Api end points for user_auth module
"""

from django.urls import path

from questionOption import views

urlpatterns = [
    path("add_question_options_for_girls/", views.add_question_options_for_girls, name="add_question_options_for_girls"),
    path("add_question_options_for_boys/", views.add_question_options_for_boys, name="add_question_options_for_boys"),
]
