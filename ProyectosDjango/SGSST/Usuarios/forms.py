from django import forms
from Usuarios.models import usuario

class FormularioUsuarios(forms.Form):
    nombreusuario=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    rol=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    idEmpleado=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    
class FormularioUser(forms.ModelForm):    
    class Meta:
        model = usuario
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']="form-control"