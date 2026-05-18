from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('filme/<int:filme_id>/', views.detalhe_filme, name='detalhe_filme'),
    
    path('comentario/<int:comentario_id>/apagar/', views.apagar_comentario, name='apagar_comentario'),
]