# from rest_framework import genericpath
from rest_framework.generics import ListAPIView
from rest_framework import generics
from django.shortcuts import render,redirect
from django.http import HttpResponse
import csv
from . models import SalesInvoice,BackupFiles
from rest_framework import viewsets
from . serializers import SalesInvoiceSerializer,BackupFilesSerializer

def index(request):
    Sales_Invoice = SalesInvoice.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=sales_invoice.csv'
    writer = csv.writer(response)
    writer.writerow(['ID','Customer Name', 'Phone', 'Address', 'Amount', 'Discount','Tax Percent','Invoice Items'])
    sales = Sales_Invoice.values_list('id','customer_name','phone', 'address', 'amount', 'discount_amount','tax_percent','invoice_items')
    for sale in sales:
        writer.writerow(sale)
    return response


class SalesInvoiceViewset(viewsets.ModelViewSet):
    queryset=SalesInvoice.objects.all()
    serializer_class=SalesInvoiceSerializer
    filterset_fields=['created_at']

# class BackupViewset(generics.ListAPIView):
#     queryset = SalesInvoice.objects.all()
#     serializer_class = SalesInvoiceSerializer          
#     def get_queryset(self):
        
#         user = self.request.user
#         return SalesInvoice.objects.filter(created_at=user)
# class BackupViewset(generics.ListCreateAPIView):
# 	queryset = SalesInvoice.objects.all()
# 	serializer_class = SalesInvoiceSerializer
# 	name = 'Sales Invoice Viewset List'	
# 	filter_fields = (
# 		'created_at',		
# 	)

class BackupFilesViewset(viewsets.ModelViewSet):
    queryset=BackupFiles.objects.all()
    serializer_class=BackupFilesSerializer



