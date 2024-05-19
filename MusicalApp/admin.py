from django.contrib import admin

# Register your models here.
from MusicalApp.models import Instrument, Brands, Cart

admin.site.register(Instrument),
admin.site.register(Brands)
admin.site.register(Cart)


