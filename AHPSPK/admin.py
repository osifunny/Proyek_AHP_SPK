from django.contrib import admin
from AHPSPK.models import *
# Register your models here.

class LaptopAdmin(admin.ModelAdmin):
    list_display = ['Laptop','Harga','RAM','Processor','Storage','Berat']
    search_fields = ['Harga','RAM','Processor','Storage','Berat']
    list_filter = ('Processor',)

admin.site.register(Laptop, LaptopAdmin)
admin.site.register(TProcessor)