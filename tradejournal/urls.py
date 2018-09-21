
from django.urls import path
from . import views

urlpatterns = [
    path('', views.journal, name='journal'),
    path('<int:journal_id>/', views.journaldetail, name='journaldetail'),
]
