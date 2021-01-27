from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import Mensagens
from .forms import MensagensForm, EditarMensagemForm

def index(request):
	return render(request, 'mensagens/index.html')


class MsgListView(generic.ListView):
    model = Mensagens

class DetailView(generic.DetailView):
    model = Mensagens

@login_required
def cadastrarMensagens(request):
	if request.method == "POST":
		form = MensagensForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('mensagens:mensagens')
	else:
		form = MensagensForm()		
	return render(request, "mensagens/cadastrar_mensagem.html", {'form':form})

@login_required
def editarMensagens(request, id):
	form_id = Mensagens.objects.get(pk=id)
	if request.method == "POST":
		form = EditarMensagemForm(request.POST, instance=form_id)
		if form.is_valid():
			form.save()
			return redirect('mensagens:detail', form_id.id)
	else:
		form = EditarMensagemForm(instance=form_id)
	return render(request, 'mensagens/editar_mensagem.html', {'form':form, 'form_id':form_id})

@login_required
def excluirMensagensBotao(request, id):
	form = Mensagens.objects.get(pk=id)
	return render(request, 'mensagens/excluir_mensagem.html', {'form':form})

@login_required
def excluirMensagens(request, id):
	form = Mensagens.objects.get(pk=id)
	form.delete()
	return redirect('mensagens:mensagens')