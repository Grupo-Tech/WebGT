from django.shortcuts import render, redirect
from .models import Post, Categoria
from django.views.generic import View
from .forms import ContactoForm
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


def home(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(
            nombre__iexact='Inicio'))

    return render(request, 'index.html', {'posts': posts})


def Acerca_de(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(
            nombre__iexact='Acerca de'))

    return render(request, 'Acerca_de.html', {'posts': posts})


def Clientes(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(
            nombre__iexact='Clientes'))
    return render(request, 'Clientes.html', {'posts': posts})


def Productos(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(
            nombre__iexact='Productos'))

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'Productos.html', {'posts': posts})


def detallePost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'detalle_post': post})


class FormularioContacto(View):
    def get(self, request, *args, **kwargs):
        form = ContactoForm()
        contexto = {
            'form': form,
        }
        return render(request, 'Contactos.html', contexto)

    def post(self, request, *args, **kwargs):
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
        else:
            contexto = {
                'form': form,
            }
            return render(request, 'Contactos.html', contexto)
