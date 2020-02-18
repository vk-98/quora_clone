from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('question/<int:pk>/', views.QuestionDetailView.as_view(), name = 'question_detail'),
    path('create/', views.QuestionCreationView.as_view(), name='create'),
    path('question/<int:pk>/answer', views.AnswerCreationView.as_view(), name = 'answer'),
]