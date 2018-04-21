from django.urls import path

from . import views


urlpatterns=[
	path('',views.index,name='index'),
	path('posts/<slug:blog_link>/',views.blog_detail,name='blog_detail'),
]
