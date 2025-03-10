from django import forms

class DateInput(forms.DateInput):
    input_type='date'

class ClienteForm(forms.Form):
    SEXO_CHOICES = (
        ('M','Masculino'),
        ('F','Femenino')
    )

    rfc = forms.CharField(label='RFC',max_length=13)
    nombre = forms.CharField(label-'Nombres',max_length=200,required=True)
    apellidos = forms.CharField(label='Apellidos',max_length=200)
    email = forms.EmailField(label='Email',required=True)
    direccion = forms.CharField(label='Direccion',widget=forms.Textarea)
    telefono = forms.CharField(label='Telefono',max_length=20)
    sexo = forms.ChoiceField(label='Sexo',choices=SEXO_CHOICES)
    fecha_nacimiento = forms.DateField(label='Fecha Nacimiento',input_formats=['%Y-%m-%d'],widget=DateInput())
