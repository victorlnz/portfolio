from email.message import EmailMessage
from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from .models import Proyectos,Correos
from .forms import CorreoForm
# Create your views here.

class HomeView(TemplateView):
    template_name = "portafolio/home.html"


class ListProyectos(ListView):
    template_name = "portafolio/list-proyectos.html"
    model = Proyectos
    context_object_name = "projects"

class EmailTemplate(TemplateView):
    template_name = "portafolio/send-email.html"

class EnviarCorreo(FormView):
    template_name= "portafolio/contacto.html"
    form_class = CorreoForm
    success_url = reverse_lazy("portafolio_app:emailTemplate")

    def form_valid(self, form):
        Correos.objects.create(
            nombre = form.cleaned_data["nombre"],
            email = form.cleaned_data["email"],
            mensaje = form.cleaned_data["mensaje"],        
        )

        
        asunto = "mensaje de cliente nuevo: " + form.cleaned_data["nombre"]
        mensaje = form.cleaned_data["mensaje"] + "cuenta de contacto:  " + form.cleaned_data["email"]
        
        send_mail(asunto,mensaje,"victor26lanza@gmail.com",['victorlnz2600@gmail.com'])  

        return super(EnviarCorreo,self).form_valid(form)

    


  



        



    

