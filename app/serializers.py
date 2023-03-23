from rest_framework import serializers
from .models import SalesInvoice,BackupFiles

class SalesInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=SalesInvoice
        fields="__all__"

class BackupFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model=BackupFiles
        fields="__all__"