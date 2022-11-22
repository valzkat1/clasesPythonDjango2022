from django import forms
from Empleados.models import empleado

class FormularioEmpleados(forms.Form):
    nombres=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    apellidos=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    tipoId=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    identificacion=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    cargo=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    doc_arl=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Documento ARL")
    doc_afp=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    doc_eps=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
class FormularioEmp(forms.ModelForm):    
    class Meta:
        model = empleado
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']="form-control"    