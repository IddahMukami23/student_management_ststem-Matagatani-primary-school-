from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-url'),
    path('<int:id>', views.view_student, name='view_student'),
]
