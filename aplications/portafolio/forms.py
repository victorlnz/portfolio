from django import forms
from .models import Correos

class CorreoForm(forms.ModelForm):

    class Meta:
        model = Correos
        fields = (
            'nombre',
            'email',
            'mensaje',
        )

        widgets = {
            "nombre":forms.TextInput(
                attrs= {
                    "placeholder":"Nombre Completo",
                    
                },
            ),
            "email":forms.TextInput(
                attrs={
                    "placeholder":"Ingrese su correo",
                    
                }
            ),
            "mensaje":forms.TextInput(
                attrs={
                    "placeholder":"Deje su mensaje",
                      
                    
                }
            )
        } 
          


        