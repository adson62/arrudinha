from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Mensagens(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	titulo_msg = models.CharField('Título da mensagem', max_length=50, blank=False, null=False)
	texto_msg = models.TextField('Mensagem', max_length=500, blank=False, null=False)
	data_pub = models.DateTimeField('Data da publicação', blank=False, null=False, default=timezone.now)
	url_foto = models.URLField('URL foto Google Drive (opcional)', blank=True, null=True, max_length=400)
	class Meta:
		ordering = ['-id',]
	def __str__(self):
		return self.titulo_msg