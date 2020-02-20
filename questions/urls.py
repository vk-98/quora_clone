from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('question/<int:pk>/', views.QuestionDetailView.as_view(), name = 'question_detail'),
    path('create/', views.QuestionCreationView.as_view(), name='create'),
    path('question/<int:pk>/answer', views.AnswerCreationView.as_view(), name = 'answer'),
    path('question/<int:pk>/update', views.QuestionUpdateView.as_view(), name = 'question_update'),
    path('question/<int:pk>/delete', views.QuestionDeleteView.as_view(), name = 'question_delete'),
    path('question/<int:pk>/answer/<int:pk1>/update', views.AnswerUpdateView.as_view(), name = 'answer_update'),
    path('question/<int:pk>/answer/<int:pk1>/delete', views.AnswerDeleteView.as_view(), name = 'answer_delete'),
]