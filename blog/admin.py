from django.contrib import admin
from .models import Post,Category,Tag,Menu,Button

class PostAdmin(admin.ModelAdmin):
	fields=['title','subtitle','publish_date','link','content','author','category','tag']
	list_display=('title','subtitle','publish_date','link','author','category')
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
class MenuAdmin(admin.ModelAdmin):
	fields=['name','link','order']
	list_display=('name','link','order')
admin.site.register(Menu,MenuAdmin)
class ButtonAdmin(admin.ModelAdmin):
	fields=['name','url','order']
	list_display=('name','url','order')
admin.site.register(Button,ButtonAdmin)
