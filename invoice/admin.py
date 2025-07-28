from django.contrib import admin
from .models import Invoice, Items

# Register your models here.
admin.site.register(Invoice)
admin.site.register(Items)