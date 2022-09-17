from django.urls import path
from loja_app.views import CreateProdutoView, DeleteProdutoView, DetailProdutoView, IndexView, ListMarcaView, CreateMarcaView, ListProdutoView, UpdateProdutoView


app_name = 'loja_app'

urlpatterns = [
    path('marca/', ListMarcaView.as_view(), name='list-marca'),
    path('marca/cadastro', CreateMarcaView.as_view(), name='create-marca'),
    

    path('', ListProdutoView.as_view(), name='list-produto'),
    path('produto/cadastro/', CreateProdutoView.as_view(), name='create-produto'),
    path('produto/<int:pk>/', DetailProdutoView.as_view(), name='detail-produto'),
    path('produto/<int:pk>/deletar/', DeleteProdutoView.as_view(), name='delete-produto'),
    path('produto/<int:pk>/update/', UpdateProdutoView.as_view(), name='update-produto'),
]