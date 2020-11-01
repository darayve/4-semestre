from django.contrib import admin
from django.urls import path
from contatos.views import lista, add, contato, editar, remover

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista/', lista),
    path('add/', add),
    path('editar/<int:nr_editcontato>', editar),
    path('contato/<int:nr_contato>', contato),
    path('remover/<int:nr_rmcontato>', remover),
]
