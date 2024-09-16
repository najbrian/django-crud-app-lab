from django.contrib import admin
from .models import Shoe, Lace, Cleaning

# Register your models here.
admin.site.register(Shoe)
admin.site.register(Cleaning)
admin.site.register(Lace)