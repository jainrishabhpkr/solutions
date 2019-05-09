from django.contrib import admin
from products.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','title','description','price','categories')
    list_display_links =('id','title')
    prepopulated_fields = {'slug':('title',)}




admin.site.register(Product, ProductAdmin)
