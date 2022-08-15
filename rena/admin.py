from django.contrib import admin
from .models import activity, student, SubmitForm

# Register your models here.

admin.site.register(activity)
admin.site.register(student)
admin.site.register(SubmitForm)
