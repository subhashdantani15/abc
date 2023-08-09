from django.contrib import admin
from app1.models import *
# Register your models here.

class Userdisplay(admin.ModelAdmin):
    list_display=['name','email','number','address']
    list_filter=['name','email','number','address']
    search_fields=['name','number']
admin.site.register(Userregister,Userdisplay)

admin.site.register(Category)


class Productdisplay(admin.ModelAdmin):
    list_display=['name','price','quantity']
admin.site.register(Product,Productdisplay)

admin.site.register(Contactus)

class Orderdisplay(admin.ModelAdmin):
    list_display=['userid','productid','price','datetime']
admin.site.register(Order,Orderdisplay)