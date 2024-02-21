"""
Api end points for user_auth module
"""

from django.urls import path

from answerOfQuestions import views

urlpatterns = [
    path("add_answers_of_girls/", views.add_answers_of_girls, name="add_answers_of_girls"),
    path("update_answers_of_girls/", views.update_answers_of_girls, name="update_answers_of_girls"),
    path("add_answers_of_boys/", views.add_answers_of_boys, name="add_answers_of_boys"),
    path("update_answers_of_boys/", views.update_answers_of_boys, name="update_answers_of_boys"),
]
