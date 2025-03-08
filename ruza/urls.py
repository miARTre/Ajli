from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('citat1/', views.citat1, name='citat1'),
    path('citat2/', views.citat2, name='citat2'),
]
