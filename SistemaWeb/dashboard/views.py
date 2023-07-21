from django.shortcuts import redirect, render,get_object_or_404
from .forms import *
from django.views import View
from django.contrib.auth import authenticate, login
from .forms import ClienteForm,VendedorForm,ProformaForm
from .models import  Cliente,Vendedor,Proforma,Bu,Pago,Moneda
# Create your views here

def inicio(request):
    return render(request,'principal.html')

def registro(request):
    data = {
        'form':CustomUserCreationForm()
    }
    if request.method =='POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect(to='inicio')

        data["form"] = formulario
    return render(request, 'registration/registro.html',data)

#-------CLIENTE--------
class ClienteView(View):
    
    def get(self,request):
        listaClientes = Cliente.objects.all()
        formCliente = ClienteForm()
        context = {
            'clientes' : listaClientes,
            'formClientes' : formCliente
        }
        return render(request,'clientes.html',context)
def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente')
    else:
        form = ClienteForm()
    return render(request, 'agregarCliente.html', {'form': form})


#---------FIN CLIENTE---------------------------
class VendedorView(View):
    def get(self,request):
        listaVendedores = Vendedor.objects.all()
        formVendedor = VendedorForm()
        context = {
            'vendedores' : listaVendedores,
            'formVendedores' : formVendedor
        }
        return render(request, 'vendedor.html',context)
    
class ProformaView(View):
    def get(self, request):
        listaProformas = Proforma.objects.all()
        context = {
            'proformas': listaProformas
        }
        return render(request, 'proforma.html', context)

class ProformaAgregarView(View):
    def get(self, request):
        formProforma = ProformaForm()

        # Obtener las listas de objetos para cada modelo
        lista_bu = Bu.objects.all()
        lista_pago = Pago.objects.all()
        lista_moneda = Moneda.objects.all()
        lista_vendedor = Vendedor.objects.all()

        context = {
            'formProforma': formProforma,
            'lista_bu': lista_bu,
            'lista_pago': lista_pago,
            'lista_moneda': lista_moneda,
            'lista_vendedor': lista_vendedor,
        }
        return render(request, 'agregar_proforma.html', context)

    def post(self, request):
        formProforma = ProformaForm(request.POST)
        if formProforma.is_valid():
            formProforma.save()
            return redirect('proforma')

        # Si el formulario no es válido, volvemos a mostrarlo con los errores
        context = {
            'formProforma': formProforma,
            'lista_bu': Bu.objects.all(),
            'lista_pago': Pago.objects.all(),
            'lista_moneda': Moneda.objects.all(),
            'lista_vendedor': Vendedor.objects.all(),
        }
        return render(request, 'agregar_proforma.html', context)

class ProformaEditarView(View):
    def get(self, request, pk):
        proforma = get_object_or_404(Proforma, pk=pk)
        formProforma = ProformaForm(instance=proforma)
        context = {
            'formProforma': formProforma,
        }
        return render(request, 'agregar_proforma.html', context)

    def post(self, request, pk):
        proforma = get_object_or_404(Proforma, pk=pk)
        formProforma = ProformaForm(request.POST, instance=proforma)
        if formProforma.is_valid():
            formProforma.save()
            return redirect('proforma')  # Redirige a la lista de Proformas después de guardar

        context = {
            'formProforma': formProforma,
        }
        return render(request, 'agregar_proforma.html', context)

class ProformaEliminarView(View):
    def post(self, request, pk):
        proforma = get_object_or_404(Proforma, pk=pk)
        if request.method == 'POST':
            proforma.delete()
            return redirect('proformas')  # Redirige a la lista de Proformas después de eliminar

        context = {
            'proforma': proforma
        }
        return render(request, 'eliminar_proforma.html', context)