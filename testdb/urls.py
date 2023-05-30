from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page),
    path("teachers/<str:teacher_id>/", views.t_detail, name = 't_detail'),
]