from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('salesInvoice', views.SalesInvoiceViewset)
router.register('backup', views.BackupFilesViewset)
# router.register('getbackup',views.BackupViewset)


urlpatterns = [
    path('index/',views.index),
    path('',include(router.urls)),
]
