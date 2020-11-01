from django import forms
from contatos.models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ('nome', 'endereco', 'celular', 'email', 'data_nascimento', 'sexo')
