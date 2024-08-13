from django.contrib import admin
from . models import WatcheDB,watchupload,wishlist,Cart,Watchreviews
# Register your models here.


admin.site.register(WatcheDB)


class watchmodeladmin(admin.ModelAdmin):
    list_display=('name','description','price','image')
    fields=['name','description','price','image']
    list_filter=('name','price')
    search_fields=['name','description']
admin.site.register(watchupload, watchmodeladmin)



class wishlistadmin(admin.ModelAdmin):
    
    fields=['user','products']
    list_filter=['user','products']
    search_fields=['user','products']



admin.site.register(wishlist,wishlistadmin)
admin.site.register(Cart,wishlistadmin)


class reviewadmin(admin.ModelAdmin):
    list_display=('user','products','review','rating')
    list_filter=['user','products']
    search_fields=['user','products']

admin.site.register(Watchreviews,reviewadmin)