from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meat_view/<mid>', views.meat_view, name='meat_view')
]