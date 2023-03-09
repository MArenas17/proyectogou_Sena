from django.forms import ModelForm, TextInput,DateTimeInput,Select,NumberInput,PasswordInput,EmailInput,ChoiceField,HiddenInput
from .models import Ruta,Publicacion,User,Servicio,Rol

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
        fields = ('tipo','descripcion','sector','establecimiento','supermercado','referencia_pago','entidad_pago','User')
        tipo_servicio = (('Selecciona una opción', 'Selecciona una opción'),('Mensajería', 'Mensajería'),('Ajuste de mercado', 'Ajuste de mercado'),('Pago de factura','Pago de factura'),('Pedimos por ti','Pedimos por ti'),('Cajero en casa','Cajero en casa'),)
        supermercado = (('Selecciona una opción', 'Selecciona una opción'),('D1','D1'),('La vaquita','La vaquita'),('Olimpica','Olimpica'),('Éxito','Éxito'),('La bodeguita','La bodeguita'),)
        widgets = {
            'tipo':Select(attrs={'class':'form-control'},choices= tipo_servicio),
            'descripcion': TextInput(attrs={'class':'form-control'}),
            'sector' :TextInput(attrs={'class':'form-control'}),
            'establecimiento': TextInput(attrs={'class':'form-control'}),
            'supermercado' :Select(attrs={'class':'form-control'},choices= supermercado),
            'referencia_pago': TextInput(attrs={'class':'form-control'}), 
            'entidad_pago': TextInput(attrs={'class':'form-control'}),
            'User': HiddenInput(attrs={'class':'form-control'}),

        }
        labels = {

            'tipo': 'Tipo de servicio que desea solicitar',
            'descripcion': 'Descripción del producto',
            'sector':'Sector o Barrio',
            'establecimiento' : 'Establecimiento',
            'supermercado' : 'Supermercado',
            'referencia_pago' : 'Referencia de pago',
            'entidad_pago' : 'Entidad a la que se le va aplicar el pago',
            
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


