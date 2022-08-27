from django.contrib import admin
from .models import Payment, userinformations,Contact_form,Tsu_MI_Details,Popular_Details,PaymentFees

# Register your models here.


class userinfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'phone')
    list_filter = ("first_name",)
    search_fields = ['first_name',  'address']
    


admin.site.register(userinformations,userinfoAdmin)


class contactFormAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'message', 'phone')
    list_filter = ("fullname",)
    search_fields = ['fullname',  'email','phone']

admin.site.register(Contact_form,contactFormAdmin)


class TsumiDetailsAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'city', 'address','category_name', 'send_type','ordered_on','fulfilled')
    list_filter = ("fullname", "city", "send_type")
    search_fields = ['fullname',  'phone', 'city', 'send_type','address']
    actions = ['Order fulfilled']


    def order_fulfilled(self, request, queryset):
        queryset.update(fulfilled=True)

admin.site.register(Tsu_MI_Details,TsumiDetailsAdmin)
    

admin.site.register(Popular_Details)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("amount", "ref", "email","date_created","verified")
    list_filter  = ("amount", "ref")
    search_fields = [list_filter]
    actions = ['Order fulfilled']
    
    def order_fulfilled(self, request, queryset):
        queryset.update(fulfilled=True)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(PaymentFees)