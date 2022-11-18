from django import forms

class FormularioEmpleados(forms.Form):
    nombres=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    apellidos=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    tipoId=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    identificacion=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    cargo=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    doc_arl=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Documento ARL")
    doc_afp=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    doc_eps=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))