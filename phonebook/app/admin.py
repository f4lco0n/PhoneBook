from django.contrib import admin
from .models import Person,Phone,Email
# Register your models here.
admin.site.register(Person)
admin.site.register(Phone)
admin.site.register(Email)