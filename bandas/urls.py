from django.urls import path
from.views import lista_bandas, new_banda, search_banda, edit_banda, delete_banda

urlpatterns = [
    path('', lista_bandas, name='list'),
    path('new', new_banda, name='new'),
    path('search', search_banda, name='search'),
    path('edit/<int:pk>', edit_banda, name='editar'),
    path('delete/<int:pk>', delete_banda, name='deletar')
]