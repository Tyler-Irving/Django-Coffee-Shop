from django.contrib import admin
from app.models import Coffee, Transaction


@admin.register(Coffee)
class CoffeAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass


# Register your models here.
