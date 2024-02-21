"""
Api end points for user_auth module
"""

from django.urls import path

from question import views

urlpatterns = [
    path("add_question_for_girls/", views.add_question_for_girls, name="add_question_for_girls"),
    path("add_question_for_boys/", views.add_question_for_boys, name="add_question_for_boys"),
    path("get_questions_with_options_for_girls/", views.get_questions_with_options_for_girls, name="get_questions_with_options_for_girls"),
    path("get_questions_with_options_for_boys/", views.get_questions_with_options_for_boys, name="get_questions_with_options_for_boys"),
]
