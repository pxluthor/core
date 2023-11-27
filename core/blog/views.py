from django.shortcuts import render
from blog.models import Post




def home(request):

    posts= Post.objects.order_by('-data_publicacao') [:5]

    context= {
        'posts': posts
    }

    return render(request,'blog/home2.html',context)


def post_detail(request, post_id):

        post= Post.objects.get(pk=post_id)

        context= {
            'post': post
    }
        return render(request,'blog/post_detail.html',context)


