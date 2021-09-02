from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dash, name='dash'),
    path('designskill/create/', views.DesignSkillCreate.as_view(), name='designskill_create'),
    path('designskill/update/<int:pk>/', views.DesignSkillUpdate.as_view(), name='designskill_update'),
    path('designskill/delete/<int:pk>/', views.DesignSkillDelete.as_view(), name='designskill_delete'),
]
