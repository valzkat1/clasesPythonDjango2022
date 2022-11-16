from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Nombre de la persona",max_length=10)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}),min_length=10)
    asunto=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    mensaje=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))