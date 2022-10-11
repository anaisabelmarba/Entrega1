from socket import fromshare
from django import forms 

class ComentraiosFormularios(forms.form):
    
    comentarios = forms.CharField()
    
    