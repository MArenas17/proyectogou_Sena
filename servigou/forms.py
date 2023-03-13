from django.forms import ModelForm, TextInput,DateTimeInput,Select,NumberInput,PasswordInput,EmailInput,ChoiceField,HiddenInput,Textarea
from .models import Ruta,Publicacion,User,Servicio,Rol, Pqrs

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
        fields = ('__all__')
        tipos = (('Seleciona una opción','Seleciona una opción'),('Mensajería','Mensajería'),('Ajustes de mercado','Ajustes de mercado'),('Cajero en casa','Cajero en casa'),('Pago de factura','Pago de factura'),('Pedimos por ti','Pedimos por ti'),)
        widgets = {
            'fecha_hora': DateTimeInput(attrs={'class':'form-control','readonly': 'readonly'}),
            'tipo': Select(attrs={'class':'form-control'}, choices=tipos),
            'sector':TextInput(attrs={'class':'form-control'}),
            'direccion':TextInput(attrs={'class':'form-control'}),
            'celular':NumberInput (attrs={'class':'form-control'}),
            'descripcion':Textarea(attrs={'class':'form-control','placeholder': 'Ejemplo : Necesito que por favor me traigan del D1 una libra de panela, de la carniceria la fama una libra de carne para sudar' }),
            'User': HiddenInput(attrs={'class':'form-control'}),

        }
        labels = {
            'fecha_hora' : 'Fecha y Hora',
            'sector': 'Sector o barrio',
            'direccion' : 'Dirección',
            'celular' : 'Celular',
            'descripcion' : '¿Que deseas solicitar?'
        }



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','documento','email','direccion','celular','password','groups' )
        help_texts = {
            'username':None,'first_name':None,'last_name':None,'password':None,
            'direccion':None,'email':None,'groups':None
        }
        widgets = {
            'username': TextInput(attrs={'class':'form-control'}),
            'first_name': TextInput(attrs={'class':'form-control'}),
            'last_name': TextInput(attrs={'class':'form-control'}),
            'documento':NumberInput (attrs={'class':'form-control'}),
            'email': EmailInput(attrs={'class':'form-control'}),
            'direccion': TextInput(attrs={'class':'form-control'}) ,
            'celular': NumberInput (attrs={'class':'form-control'}),
            'password': PasswordInput(attrs={'class':'form-control'}) ,
            'groups' : Select(attrs={'class':'form-control'})
        }
        labels = {
            'documento':'Documento',
            'celular' : 'Número de Celular',
            'direccion': 'Dirección de residencia',
            'email': 'Email',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'groups' : 'Rol'
        }

class RolForm(ModelForm):
    class Meta:
        model = Rol
        fields = '__all__'
        widgets = {
            'nombre_rol ': TextInput(attrs={'class':'form-control'}),
            'nivel_permiso': NumberInput (attrs={'class':'form-control'}),
            },
        labels = {
            'nombre_rol':'Rol',
            'nivel_permiso' : 'Nivel de permiso',
        }

class PqrsForm(ModelForm):
    class Meta:
        model = Pqrs
        fields = '__all__'
        asunto = (('Selecione una opción','Selecione una opción'),('Peticiones','Peticiones'),('Quejas','Quejas'),('Reclamos','Reclamos'),('Sugerencias','Sugerencias'),('Felicitaciones','Felicitaciones'),)
        widgets = {
            'nombre': TextInput(attrs={'class':'form-control'}),
            'email': EmailInput(attrs={'class':'form-control'}),
            'asunto': Select(attrs={'class':'form-control'}, choices=asunto),
            'mensaje': Textarea(attrs={'class':'form-control'}),
            'User' : HiddenInput
        }
        labels = {
            'nombre':'Nombre',
            'email':'Correo Electrónico',
            'asunto':'Asunto',
            'mensaje':'Mensaje',
        }
