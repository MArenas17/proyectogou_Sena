from django.forms import ModelForm, TextInput, DateTimeInput, Select, NumberInput, PasswordInput, EmailInput, \
    HiddenInput, Textarea

from .models import Ruta, Publicacion, User, Servicio, Rol, Pqrs


class PublicacionForm(ModelForm):
    class Meta:
        model = Publicacion
        fields = '__all__'
        widgets = {
            'nombre_publicacion': TextInput(attrs={'class': 'form-control'}),
            'tipo_archivo': TextInput(attrs={'class': 'form-control'}),
            'User': Select(attrs={'class': 'form-control'})
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
            'valor_km': NumberInput(attrs={'class': 'form-control'}),
            'km': NumberInput(attrs={'class': 'form-control'}),
            'porcentaje_liquidacion': NumberInput(attrs={'class': 'form-control'}),
            'incremento': NumberInput(attrs={'class': 'form-control'}),
            'total_servicio': NumberInput(attrs={'class': 'form-control'}),
            'total_liquidacion': NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'valor_km': 'Valor por km',
            'km': 'kilometros',
            'porcentaje_liquidacion': 'Porcentaje a liquidar',
            'incremento': 'Incremento del servicio',
            'total_servicio': 'Total a pagar',
            'total_liquidacion': 'Total a liquidar'
        }


class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        exclude = ['Repartidor']
        tipos = (('Seleciona una opción', 'Seleciona una opción'), ('Mensajería', 'Mensajería'),
                 ('Ajustes de mercado', 'Ajustes de mercado'), ('Cajero en casa', 'Cajero en casa'),
                 ('Pago de factura', 'Pago de factura'), ('Pedimos por ti', 'Pedimos por ti'),)
        sector = (
            ('Seleciona una opción', 'Seleciona una opción'),
            ('Naranjal', 'Naranjal'),
            ('El llano', 'El llano'),
            ('Los Piedrahita', 'Los Piedrahita'),
            ('Los Uribe', 'Los Uribe'),
            ('Travesias', 'Travesias'),
            ('La cumbre', 'La cumbre'),
            ('La bocadillera', 'La bocadillera'),
            ('Aguas frias', 'Aguas frias'),
            ('Palenque', 'Palenque'),
            ('Chambacú', 'Chambacú'),
            ('Los Galpones', 'Los Galpones'),
            ('La Ladrillera', 'La Ladrillera'),
            ('El tejar', 'El tejar'),
            ('Barrio Nuevo', 'Barrio Nuevo'),
            ('El Hueco', 'El Hueco'),
            ('Las playas', 'Las playas'),
            ('El uvito', 'El uvito'),
            ('la cuchilla', 'la cuchilla'),
            ('EL patio', 'EL patio'),
            ('La palma', 'La palma'),
            ('El Parque', 'El Parque'),
            ('Playa Rica', 'Playa Rica'),
            ('El Cristo', 'El Cristo'),
            ('Calle negra', 'Calle negra'),
            ('balmoral', 'balmoral'),
            ('Caracoli', 'Caracoli'),
            ('Avellanas', 'Avellanas'),
            ('Regina 11', 'Regina 11'),
            ('Roblemar', 'Roblemar'),
            ('Palacio de las Fresas', 'Palacio de las Fresas'),
            ('La Y', 'La Y'),
            ('Las Margaritas', 'Las Margaritas'),
            ('La Cascada', 'La Cascada'),
            ('Vallejuelos', 'Vallejuelos'),
            ('El porvenir', 'El porvenir'),
            ('Fuente Clara', 'Fuente Clara'),
            ('Robledo Parque', 'Robledo Parque'),
            ('Exito de Robledo', 'Exito de Robledo'),
            ('Calle del comercio', 'Calle del comercio'),
            ('Cuatro Esquinas', 'Cuatro Esquinas'),
            ('La Perez', 'La Perez'),
            ('Cocondo', 'Cocondo'),
            ('Pedregal Alto', 'Pedregal Alto'),
            ('Paulandia', 'Paulandia'),
            ('Rancho grande', 'Rancho grande'),
            ('La Cárcel', 'La Cárcel'),
            ('Predregal Bajo', 'Predregal Bajo'),
            ('Los locos', 'Los locos'),
            ('Las Hamacas', 'Las Hamacas'),
            ('Las Partidas San Pedro - Via al Mar', 'Las Partidas San Pedro - Via al Mar'),
            ('Yolombo', 'Yolombo'),
            ('La Ilusión', 'La Ilusión'),
            ('San Jose de la Montaña', 'San Jose de la Montaña'),
            ('La Zeca', 'La Zeca'),
            ('Alto de Boquerón', 'Alto de Boquerón'),
            ('La Cajetilla', 'La Cajetilla'),
            ('EL Hueco de Boquerón', 'EL Hueco de Boquerón'),
            ('Pajarito', 'Pajarito'),
            ('La campiña', 'La campiña'),
            ('la Pola', 'la Pola'),
            ('La Huerta', 'La Huerta'),
            ('La loma', 'La loma'),
            ('San Javier', 'San Javier'),
            ('Las Américas', 'Las Américas'),
            ('Envigado', 'Envigado'),
            ('Poblado', 'Poblado'),
            ('Aguacatala', 'Aguacatala'),
            ('Itagui', 'Itagui'),
            ('Sabaneta', 'Sabaneta'),
            ('La Estrella', 'La Estrella'),
            ('Caldas', 'Caldas'),
            ('Bello', 'Bello'),
            ('Copacabana', 'Copacabana'),
            ('Girardota', 'Girardota'),
            ('Villa Nueva', 'Villa Nueva'),
            ('Villa Hermosa', 'Villa Hermosa'),
            ('Prado', 'Prado'),
            ('Prado Centro', 'Prado Centro'),
            ('Boston', 'Boston'),
            ('Enciso', 'Enciso'),
            ('Enciso los Mangos', 'Enciso los Mangos'),
            ('La sierra', 'La sierra'),
            ('Buenos Aires', 'Buenos Aires'),
            ('Santa Helena', 'Santa Helena'),
            ('Popular', 'Popular'),
            ('Santa Cruz', 'Santa Cruz'),
            ('Manrrique', 'Manrrique'),
            ('Aranjuez', 'Aranjuez'),
            ('La Candelaria', 'La Candelaria'),
            ('Castilla', 'Castilla'),
            ('12 de Octubre', '12 de Octubre'),
            ('Robledo', 'Robledo'),
            ('Laureles Estadio', 'Laureles Estadio'),
            ('Belén', 'Belén'),
            ('Guayabal', 'Guayabal'),
            ('Altavista', 'Altavista'),
            ('San Antonio de Prado', 'San Antonio de Prado'),
            ('Centro de Medellín', 'Centro de Medellín'),
            ('Laureles', 'Laureles'),
            ('Jalisco', 'Jalisco'),
            ('El Carmelo', 'El Carmelo'),
            ('El picacho', 'El picacho'),
            ('Waira', 'Waira'),
            ('San Felix', 'San Felix'),
            ('Charco Verde', 'Charco Verde'),
            ('Ovejas', 'Ovejas'),
            ('La China', 'La China'),
            ('El Tambo', 'El Tambo'),
            ('San Pedro De los Milagros', 'San Pedro De los Milagros'),
            ('La Aurora', 'La Aurora'),
            ('Las Flores', 'Las Flores'),
            ('Cantares 1-2-4', 'Cantares 1-2-4'),
            ('Cantares 3', 'Cantares 3'),
            ('Urbanización la montaña', 'Urbanización la montaña'),
            ('Urbanización mirador de la montaña', 'Urbanización mirador de la montaña'),
            ('Urbanizacion La Cascada', 'Urbanizacion La Cascada'),
            ('Urbanización Renaceres', 'Urbanización Renaceres'),
            ('Conjunto Residencial Atardeceres', 'Conjunto Residencial Atardeceres'),
            ('Unidad Residencial Portón De Occidente', 'Unidad Residencial Portón De Occidente'),
            ('Urbanización Nuevo Nazareth', 'Urbanización Nuevo Nazareth'),
            ('Colinas de Occidente', 'Colinas de Occidente'),
            ('Mirador del Valle', 'Mirador del Valle'),
            ('Tirol 1 ó 2', 'Tirol 1 ó 2'),
            ('Tirol 3', 'Tirol 3'),
        )
        widgets = {
            'fecha_hora': DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tipo': Select(attrs={'class': 'form-control'}, choices=tipos),
            'sector': Select(attrs={'class': 'form-control'}, choices=sector),
            'direccion': TextInput(attrs={'class': 'form-control'}),
            'celular': NumberInput(attrs={'class': 'form-control'}),
            'descripcion': Textarea(attrs={'class': 'form-control',
                                           'placeholder': 'Ejemplo : Necesito que por favor me traigan del D1 una libra de panela, de la carniceria la fama una libra de carne para sudar'}),
            'estado': HiddenInput,
            'User': HiddenInput(attrs={'class': 'form-control'}),

        }
        labels = {
            'fecha_hora': 'Fecha y Hora',
            'sector': 'Sector o barrio en el que Se va hacer la entrega',
            'direccion': 'Dirección',
            'celular': 'Celular',
            'descripcion': '¿Que deseas solicitar?'
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'documento', 'email', 'direccion', 'celular', 'password', 'groups')
        help_texts = {
            'username': None, 'first_name': None, 'last_name': None, 'password': None,
            'direccion': None, 'email': None, 'groups': None
        }
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'documento': NumberInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'direccion': TextInput(attrs={'class': 'form-control'}),
            'celular': NumberInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
            'groups': Select(attrs={'class': 'form-control'})
        }
        labels = {
            'documento': 'Documento',
            'celular': 'Número de Celular',
            'direccion': 'Dirección de residencia',
            'email': 'Email',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'groups': '¿Qué rol tienes en GO!?',
        }


class AsignacionForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Repartidor'].queryset = User.objects.filter(groups__name='Repartidor')

    class Meta:
        model = Servicio
        exclude = {'estado', 'User', 'sector', 'direccion','celular','descripcion','tipo','fecha_hora'}
        widgets = {'Repartidor': Select(attrs={'class': 'form-control'})}



class UserForm2(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'direccion', 'celular')
        help_texts = {
            'username': None, 'first_name': None, 'last_name': None, 'password': None,
            'direccion': None, 'email': None, 'groups': None
        }
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'documento': NumberInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'direccion': TextInput(attrs={'class': 'form-control'}),
            'celular': NumberInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
            'groups': Select(attrs={'class': 'form-control'})
        }
        labels = {
            'documento': 'Documento',
            'celular': 'Número de Celular',
            'direccion': 'Dirección de residencia',
            'email': 'Email',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'groups': '¿Qué rol tienes en GO!?',
        }


class RolForm(ModelForm):
    class Meta:
        model = Rol
        fields = '__all__'
        widgets = {
            'nombre_rol ': TextInput(attrs={'class': 'form-control'}),
            'nivel_permiso': NumberInput(attrs={'class': 'form-control'}),
        },
        labels = {
            'nombre_rol': 'Rol',
            'nivel_permiso': 'Nivel de permiso',
        }


class PqrsForm(ModelForm):
    class Meta:
        model = Pqrs
        fields = '__all__'
        asunto = (('Selecione una opción', 'Selecione una opción'), ('Peticiones', 'Peticiones'), ('Quejas', 'Quejas'),
                  ('Reclamos', 'Reclamos'), ('Sugerencias', 'Sugerencias'), ('Felicitaciones', 'Felicitaciones'),)
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'asunto': Select(attrs={'class': 'form-control'}, choices=asunto),
            'mensaje': Textarea(attrs={'class': 'form-control'}),

        }
        labels = {
            'nombre': 'Nombre',
            'email': 'Correo Electrónico',
            'asunto': 'Asunto',
            'mensaje': 'Mensaje',
        }
