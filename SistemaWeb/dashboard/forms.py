from django import forms
from .models import Cliente,Vendedor,Direccion,Moneda,Pago,Bu,Proforma
from django.contrib.auth.forms import UserCreationForm

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = '__all__'

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = '__all__'

class MonedaForm(forms.ModelForm):
    class Meta:
        model = Moneda
        fields = '__all__'

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = '__all__'

class BuForm(forms.ModelForm):
    class Meta:
        model = Bu
        fields = '__all__'

class ProformaForm(forms.ModelForm):
    class Meta:
        model = Proforma
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
     pass  