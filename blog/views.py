from django.shortcuts import render,get_object_or_404
from .models import Post,Menu,Button


def index(request):
	post_list=Post.objects.all().order_by('-publish_date')
	list_inline_item=Button.objects.all().order_by('order')
	navigation_menu_list=Menu.objects.all().order_by('order')
	return render(request,'blog/index.html',{'post_list':post_list,'list_inline_item':list_inline_item,'menu_list':navigation_menu_list})

def blog_detail(request,blog_link):
	post=get_object_or_404(Post,link=blog_link)
	return render(request,'blog/post.html',{'post':post})
