from django.shortcuts import render, get_object_or_404
from contatos.models import Contato
from contatos.forms import ContatoForm
import datetime

# Create your views here.

# Listar contatos

def lista(request):
  lista_contatos = Contato.objects.all()

  return render(request, "lista.html", {
    'lista_contatos': lista_contatos
  })

# Adicionar contato

def add(request):
  if request.method == "POST":
    form = ContatoForm(request.POST)
    if form.is_valid():
      form.save()
      return render(request, "salvo.html", {})
  else:
    form = ContatoForm()
  
  return render(request, "add.html", {
    'form': form
  })

# Página do contato

def contato(request, nr_contato):
  contato = get_object_or_404(Contato, pk=nr_contato)
  return render(request, "contato.html", {
    'contato': contato
  })

# Editar contato

def editar(request, nr_editcontato):
  edit_contato = get_object_or_404(Contato, pk=nr_editcontato)
  nascimento = edit_contato.data_nascimento
  string_data = nascimento.strftime('%Y-%m-%d')
  form = ContatoForm(instance=edit_contato)

  if request.method == "POST":
    form = ContatoForm(request.POST, instance=edit_contato)

    if form.is_valid():
      edit_contato = form.save()
      edit_contato.save()

      return render(request, "salvo.html", {})
    else:
      return render(request, "editar.html", {
          'form': form,
          'edit_contato': edit_contato
      })
  else:
      return render(request, "editar.html", {
          'form': form,
          'edit_contato': edit_contato,
          'string_data': string_data
      })

# Remover contato

def remover(request, nr_rmcontato):
  Contato.objects.filter(id=nr_rmcontato).delete()
  lista_contatos = Contato.objects.all()
  
  return render(request, "lista.html", {
      'lista_contatos': lista_contatos
  })

