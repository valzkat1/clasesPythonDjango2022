from django import forms

class FormularioUsuarios(forms.Form):
    nombreusuario=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    rol=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    idEmpleado=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))