from django.contrib import admin
from .models import userinformations

# Register your models here.


class userinfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'phone')
    list_filter = ("first_name",)
    search_fields = ['first_name',  'address']
    


admin.site.register(userinformations,userinfoAdmin)