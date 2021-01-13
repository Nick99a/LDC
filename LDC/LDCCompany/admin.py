from django.contrib import admin
from .models import BackUpCopy, Tariff, paid_receipt, Receipt, TelephoneConversation, Client, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('login','password','id_receipt','id_client')

@admin.register(paid_receipt)
class paid_receiptAdmin(admin.ModelAdmin):
    list_display = ('id_receipt','payment')

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('number','date','cost','payment_term','id_paid','id_tariff','id_tconversation')

@admin.register(TelephoneConversation)
class TelephoneConversationAdmin(admin.ModelAdmin):
    list_display = ('date','city','number','call_duration','id_conversation')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('number','firstname','lastname','address','registration_date','id_receipt')

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('date','settlment','cost_per_minute','preferential_cost')

@admin.register(BackUpCopy)
class BackUpCopyAdmin(admin.ModelAdmin):
    list_display = ('name_of_copy','type_of_copy','creation_date','commentary')

