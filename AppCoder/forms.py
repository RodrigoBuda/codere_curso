from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    
class VendedorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()

class CompraFormulario(forms.Form):
    producto = forms.CharField()
    precio = forms.IntegerField()
    enviado = forms.BooleanField()
