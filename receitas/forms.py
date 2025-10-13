from django import forms
from.models import Receitas

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receitas
        fields = ['titulo', 'descricao', 'instrucoes']
