from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dash, name='dash'),

    path('skills/', views.skills_list, name='skills_list'),

    path('designskill/create/', views.DesignSkillCreate.as_view(), name='designskill_create'),
    path('designskill/update/<int:pk>/', views.DesignSkillUpdate.as_view(), name='designskill_update'),
    path('designskill/delete/<int:pk>/', views.DesignSkillDelete.as_view(), name='designskill_delete'),

    path('codingskill/create/', views.CodingSkillCreate.as_view(), name='codingskill_create'),
    path('codingskill/update/<int:pk>/', views.CodingSkillUpdate.as_view(), name='codingskill_update'),
    path('codingskill/delete/<int:pk>/', views.CodingSkillDelete.as_view(), name='codingskill_delete'),

    path('languageskill/create/', views.LanguageSkillCreate.as_view(), name='languageskill_create'),
    path('languageskill/update/<int:pk>/', views.LanguageSkillUpdate.as_view(), name='languageskill_update'),
    path('languageskill/delete/<int:pk>/', views.LanguageSkillDelete.as_view(), name='languageskill_delete'),

    path('messages/', views.message_list, name='message_list'),
    path('message/<pk>/<name>/', views.message_detail, name='message_detail'),
]
