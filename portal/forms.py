from django import forms
from .models import Noticia, Area

class AreaForm(forms.ModelForm):
    
    class Meta:
        model = Area
        fields = ('descricao','cor', 'status',)
        
        
        
class NoticiaForm(forms.ModelForm):
    
    class Meta:
        model = Noticia
        fields = ('foto','titulo', 'texto',)
        
        
        