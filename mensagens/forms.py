from django import forms
from .models import Mensagens

class MensagensForm(forms.ModelForm):
	class Meta:
		model = Mensagens
		fields = ('usuario', 'titulo_msg', 'texto_msg', 'url_foto', 'data_pub',)

class EditarMensagemForm(forms.ModelForm):
	class Meta:
		model = Mensagens
		fields = ('titulo_msg', 'texto_msg', 'url_foto',)