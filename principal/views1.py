from django.shortcuts import render, redirect
from principal.models import *
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import *
from .models import Actividades 

def Login(request):

    return render(request, "login.html")

def Perfil(request):

    return render(request, "perfil.html")

def Home(request):

    return render(request, "GENERAL/index.html")

def Parametros1(request):

    return render(request, "GENERAL/index.html")

#Vista de el atajo para la tabla Documentos 
def crear_beneficiario(request):
    if request.method == 'POST':
        form = BeneficiarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El beneficiario se ha creado correctamente.')
            return redirect('principal2:leerProyectos')  
        else:
            messages.error(request, 'Hubo un error al crear el beneficiario.')
    else:
        form = BeneficiarioForm()
    return render(request, 'crear_beneficiario.html', {'form': form})

#---------------------------Vistas para Actividades-----------------------------------#
class ListadoActividades(SuccessMessageMixin, CreateView, ListView):
    model = Actividades
    fields = "__all__"
    queryset = Actividades.objects.all()
    success_message = 'Actividad creada satisfactoriamente'
    
    def get_success_url(self):        
        return reverse('principal1:leerActividades')

class ActividadesDetalle(DetailView):
    model = Actividades

class ActividadesActualizar(SuccessMessageMixin, UpdateView):
    model = Actividades
    fields = "__all__"
    success_message = 'Actividad actualizada satisfactoriamente'
    
    def get_success_url(self):               
        return reverse('principal1:leerActividades')

class ActividadesEliminar(SuccessMessageMixin, DeleteView): 
    model = Actividades
    
    def get_success_url(self): 
        success_message = 'Actividad eliminada satisfactoriamente' 
        messages.success(self.request, success_message)       
        return reverse('principal1:leerActividades')
#---------------------------Fin de Vistas para Actividades---------------------------------#    

#---------------------------Vistas para Beneficiarios-----------------------------------#
class ListadoBeneficiarios(SuccessMessageMixin, CreateView, ListView):
    model = Beneficiarios
    fields = "__all__"
    queryset = Beneficiarios.objects.all()
    success_message = 'Beneficiario creado satisfactoriamente'
    
    def get_success_url(self):        
        return reverse('principal1:leerBeneficiarios')

class BeneficiariosDetalle(DetailView):
    model = Beneficiarios

class BeneficiariosActualizar(SuccessMessageMixin, UpdateView):
    model = Beneficiarios
    fields = "__all__"
    success_message = 'Beneficiario actualizado satisfactoriamente'
    
    def get_success_url(self):               
        return reverse('principal1:leerBeneficiarios')

class BeneficiariosEliminar(SuccessMessageMixin, DeleteView): 
    model = Beneficiarios
    
    def get_success_url(self): 
        success_message = 'Beneficiario eliminado satisfactoriamente'
        messages.success(self.request, success_message)       
        return reverse('principal1:leerBeneficiarios')
#---------------------------Fin de Vistas para Beneficiarios-------------------------#  
  
#---------------------------Vistas para Documentos-----------------------------------#
class ListadoDocumentos(SuccessMessageMixin, CreateView, ListView):
    model = Documentos
    fields = "__all__"
    queryset = Documentos.objects.all()
    success_message = 'Documento creado correctamente'
    
    def get_success_url(self):        
        return reverse('principal1:leerDocumentos')

class DocumentosDetalle(DetailView):
    model = Documentos

class DocumentosActualizar(SuccessMessageMixin, UpdateView):
    model = Documentos
    fields = "__all__"
    success_message = 'Documento actualizado correctamente'
    
    def get_success_url(self):               
        return reverse('principal1:leerDocumentos')

class DocumentosEliminar(SuccessMessageMixin, DeleteView): 
    model = Documentos
    
    def get_success_url(self): 
        success_message = 'Documento eliminado correctamente'
        messages.success(self.request, success_message)       
        return reverse('principal1:leerDocumentos')
    
#---------------------------Vistas para Beneficiarios_Proyectos------------------------------------#
class ListadoBeneficiariosProyectos(SuccessMessageMixin,ListView):
    model = BeneficiariosProyectos
    fields = "__all__"
    queryset = BeneficiariosProyectos.objects.all()
    
    def get_success_url(self):        
        return reverse('principal1:leerBeneficiariosProyectos')

class BeneficiariosProyectosActualizar(SuccessMessageMixin, UpdateView):
    model = BeneficiariosProyectos
    fields = "__all__"
    success_message = 'Documento actualizado correctamente'
    
    def get_success_url(self):               
        return reverse('principal1:leerBeneficiariosProyectos')
    
class BeneficiariosProyectosEliminar(SuccessMessageMixin, DeleteView):
    model = BeneficiariosProyectos

    def get_success_url(self): 
        success_message = 'Documento eliminado correctamente'
        messages.success(self.request, success_message)       
        return reverse('principal1:leerBeneficiariosProyectos')