from django.contrib import admin
from receipt_api.models import Receipt, Item

# Register your models here.
admin.site.register(Receipt)
admin.site.register(Item)