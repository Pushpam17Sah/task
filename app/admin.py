from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.SalesInvoice)
admin.site.register(models.BackupFiles)

