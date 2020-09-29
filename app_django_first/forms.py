from django import forms
from app_django_first.models import Cliente


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    observacao = forms.CharField(widget=forms.Textarea)


class ModeFormClient(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
