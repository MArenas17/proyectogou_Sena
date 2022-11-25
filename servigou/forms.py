from django.forms import ModelForm, TextInput,DateTimeInput,Select,NumberInput,PasswordInput,EmailInput
from .models import Ruta,Publicacion,User,Servicio

class PublicacionForm(ModelForm):
    class Meta:
        model =  Publicacion
        fields = '__all__'
        widgets = {
            'nombre_publicacion':TextInput(attrs={'class':'form-control'}),
            'tipo_archivo':TextInput(attrs={'class':'form-control'}),
            'User': Select(attrs={'class':'form-control'})
        }

        labels = {  
            'nombre_publicacion': 'Nombre de la publicación',
            'tipo_archivo': 'Tipo de archivo',
        }

class RutaForm(ModelForm):
    class Meta:
        model = Ruta
        fields = '__all__'
        widgets = {
            'valor_km' :NumberInput (attrs={'class':'form-control'}),
            'km':NumberInput (attrs={'class':'form-control'}),
            'porcentaje_liquidacion':NumberInput(attrs={'class':'form-control'}),
            'incremento' : NumberInput (attrs={'class':'form-control'}),
            'total_servicio' : NumberInput(attrs={'class':'form-control'}),
            'total_liquidacion': NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
            'valor_km':'Valor por km',
            'km' : 'kilometros',
            'porcentaje_liquidacion': 'Porcentaje a liquidar',
            'incremento': 'Incremento del servicio',
            'total_servicio': 'Total a pagar',
            'total_liquidacion': 'Total a liquidar'
        }


class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'
        widgets = {
            'fecha_hora': DateTimeInput(attrs={'type':'date','class':'form-control'}),
            'estado_servicio':TextInput(attrs={'class':'form-control'}),
            'producto':TextInput(attrs={'class':'form-control'}),
            'User':Select(attrs={'class':'form-control'}),
            'ruta':Select(attrs={'class':'form-control'}),
        }
        labels = {
            'User':'Usuario',
            'fecha_hora' : 'Fecha y Hora',
            'estado_servicio': 'Estado del servicio',
            'producto': 'Producto',
            'ruta': 'Ruta'
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ['user_permissions','is_staff','is_active','is_superuser','last_login','date_joined','groups',]
        help_texts = {
            'username':None,'first_name':None,'last_name':None,'password':None,
            'direccion':None,'email':None,'groups':None
        }
        widgets = {
            'username': TextInput(attrs={'class':'form-control'}),
            'first_name': TextInput(attrs={'class':'form-control'}),
            'last_name': TextInput(attrs={'class':'form-control'}) ,
            'password': PasswordInput(attrs={'class':'form-control'}) ,
            'direccion': TextInput(attrs={'class':'form-control'}) ,
            'email': EmailInput(attrs={'class':'form-control'}),
            'documento':NumberInput (attrs={'class':'form-control'}),
            'celular': NumberInput (attrs={'class':'form-control'}),
        }
        labels = {
            'documento':'Documento',
            'celular' : 'Número de Celular',
            'direccion': 'Dirección'
        }