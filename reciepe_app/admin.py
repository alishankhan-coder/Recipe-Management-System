from django.contrib import admin
from django.utils.html import format_html
from .models import *
# Register your models here.



class myModalAdmin(admin.ModelAdmin):
    list_display = ('recipe_name','recipe_disc','recipe_created_at','us','image_tag')
    list_filter = ('recipe_name','recipe_created_at')
    ordering = ('recipe_created_at','user')
    search_fields = ('recipe_name',)
    def us(self,obj):
        return format_html('<h1 style="color:#264b5d;font-weight:bold;">{}</h1>',obj.user)
    us.allow_tags = True
    def image_tag(self,obj):
        return format_html('<img src="{}" width="100" height="100"/>',obj.recipe_img.url)
    # .format(obj.recipe_img.url)
    image_tag.short_description = "Image"
    image_tag.allow_tags = True
admin.site.register(Recipe,myModalAdmin)

