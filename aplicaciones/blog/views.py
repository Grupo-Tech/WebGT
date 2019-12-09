from django.shortcuts import render
from .models import Post,Categoria

def home(request):
	posts = Post.objects.filter(
		estado = True, 
		categoria = Categoria.objects.get(
			nombre__iexact = 'Inicio'))

	return render(request,'index.html',{'posts':posts})

def Acerca_de(request):
	posts = Post.objects.filter(
		estado = True, 
		categoria = Categoria.objects.get(
			nombre__iexact = 'Acerca de'))

	return render(request,'Acerca_de.html',{'posts':posts})

def Clientes(request):
	posts = Post.objects.filter(
		estado = True, 
		categoria = Categoria.objects.get(
			nombre__iexact = 'Clientes'))
	return render(request,'Clientes.html',{'posts':posts})

def Productos(request):
	posts = Post.objects.filter(
		estado = True, 
		categoria = Categoria.objects.get(
			nombre__iexact = 'Productos'))
	return render(request,'Productos.html',{'posts':posts})

def Contactos(request):
	posts = Post.objects.filter(
		estado = True, 
		categoria = Categoria.objects.get(
			nombre__iexact = 'Contactos'))
	return render(request,'Contactos.html',{'posts':posts})