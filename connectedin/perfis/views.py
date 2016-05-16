from django.shortcuts import render
from perfis.models import Perfil

def index(request):
	return render(request, 'index.html')

def exibir(request, perfil_id):
	
	perfil = Perfil()

	if perfil_id == '1':
		perfil = Perfil('Carlos Eduardo', 'carlos.eduardo@gmail.com', '99999', 'Google Inc')

	if perfil_id == '2':
		perfil = Perfil('Hermes', 'hermes@gmail.com', '8888', 'Apple')


	return render(request, 'perfil.html', {"perfil" : perfil })
