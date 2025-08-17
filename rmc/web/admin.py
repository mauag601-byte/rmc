from django.contrib import admin
from .models import Producto, Category, Compatibility

admin.site.register(Producto)
admin.site.register(Category)
admin.site.register(Compatibility)
