from django import forms
from ventas.models import Cliente, Producto

class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nombre', 'telefono')
        labels = {
            'codigo': 'Codigo cliente: ',
            'nombre': 'Nombre cliente',
            'telefono':'Telefono: (Contacto):'
        }

class EditarClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nombre', 'telefono')
        labels = {
            'codigo': 'Codigo cliente: ',
            'nombre': 'Nombre cliente',
            'telefono':'Telefono: (Contacto):'
        }
    widgets = {
        'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}),
        'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
        'telefono': forms.TextInput(attrs={'id': 'telefono_editar'}),
    }

class AddProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo', 'descripcion', 'imagen', 'costo', 'precio', 'cantidad')
        labels = {
            'codigo': 'Codigo cliente: ',
            'descripcion': 'Descripcion de producto',
            'imagen':'Imagen: ',
            'costo':'Costo $: ',
            'precio':'Precio $: ',
            'cantidad':'Cantidad: '
        }