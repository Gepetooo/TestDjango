from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'descricao', 'concluida']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            for field_name in ['nome', 'descricao']:
                self.fields[field_name].widget.attrs['placeholder'] = getattr(self.instance, field_name)
                self.initial[field_name] = ''
            self.fields['nome'].required = False

    def clean(self):
        cleaned_data = super().clean()
        if self.instance and self.instance.pk:
            for field_name in ['nome', 'descricao']:
                if not cleaned_data.get(field_name):
                    cleaned_data[field_name] = getattr(self.instance, field_name)
        return cleaned_data