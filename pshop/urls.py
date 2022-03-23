from django.urls import path
from pshop import views

app_name = 'pshop'

urlpatterns = [
    path('', views.index, name='index'),
    path('list_cliente', views.ClientesList.as_view(), name='list_cliente'),
    path('create_cliente',
         views.ClienteCreate.as_view(),
         name='create_cliente'),
    path('update_cliente/<int:pk>/',
         views.ClienteUpdate.as_view(),
         name='update_cliente'),
    path('delete_cliente/<int:pk>/',
         views.ClienteDelete.as_view(),
         name='delete_cliente'),
    path('list_pet', views.PetList.as_view(), name='list_pet'),
    path('create_pet', views.PetCreate.as_view(), name='create_pet'),
    path('update_pet/<int:pk>/', views.PetUpdate.as_view(), name='update_pet'),
    path('delete_pet/<int:pk>/', views.PetDelete.as_view(), name='delete_pet'),
    path('list_servico', views.ServicoList.as_view(), name='list_servico'),
    path('create_servico',
         views.ServicoCreate.as_view(),
         name='create_servico'),
    path('update_servico/<int:pk>/',
         views.ServicoUpdate.as_view(),
         name='update_servico'),
    path('delete_servico/<int:pk>/',
         views.ServicoDelete.as_view(),
         name='delete_servico'),
    path('about', views.about, name='about'),
]