from django import forms
from Ausentismos.models import ausentismo

class FormularioAusentismos(forms.Form):
    nombres=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    apellidos=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    tipoId=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    identificacion=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    cargo=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    eps=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="EPS")
    salario=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    tipoIncapacidad=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    salarioDia=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    fechaInicial=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
    fechaFinal=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
    

class FormularioIncapacidades(forms.ModelForm):    
    class Meta:
        model = ausentismo
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.fields['salario'].widget.attrs['onblur'] = 'calcularSalarioDia()'
        self.fields['salarioDia'].widget.attrs['readonly']='readonly'
       # self.fields['totalEmpresa'].widget = forms.HiddenInput()
       # self.fields['totalArl'].widget = forms.HiddenInput()
       # self.fields['totalAFP'].widget = forms.HiddenInput()
       # self.fields['totalEPS'].widget = forms.HiddenInput()
       # self.fields['totalIncapacidad'].widget = forms.HiddenInput()
        #self.fields['fechaInicial'].widget = forms.DateInput(attrs={'class':'form-control'})
        for field in self.fields.values():
            field.widget.attrs['class']="form-control"       
