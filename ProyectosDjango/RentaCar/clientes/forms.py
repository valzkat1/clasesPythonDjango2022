from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    asunto=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    mensaje=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))