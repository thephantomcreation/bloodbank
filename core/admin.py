from django.contrib import admin
from .models import Donor, Contact, Test, Blood

admin.site.register(Donor)
admin.site.register(Contact)
admin.site.register(Blood)
