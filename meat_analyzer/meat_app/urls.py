from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('meat_view/<mid>', views.meat_view, name='meat_view'),
    path('add_data', views.add_data, name='add_data'),
]