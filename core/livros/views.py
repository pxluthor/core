from django.shortcuts import render
from blog.models import Post

# Create your views here.

#def livros(request):
 #   return render(request, 'livros/livros.html')

def livros(request):

    posts= Post.objects.order_by('-data_publicacao') [:5]

    context= {
        'posts': posts
    }

    return render(request,'livros/livros.html',context)