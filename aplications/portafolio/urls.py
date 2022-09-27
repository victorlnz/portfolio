from django.urls import path
from . import views

app_name = "portafolio_app"

urlpatterns = [
    path(
        '',
        views.HomeView.as_view(),
        name="home"
    ),
    path(
        'proyectos',
        views.ListProyectos.as_view(),
        name="proyectos"),
    path(
        'contacto',
        views.EnviarCorreo.as_view(),
        name="contactos"),
    path(
        'emailTemplate',
        views.EmailTemplate.as_view(),
        name="emailTemplate"),        
]