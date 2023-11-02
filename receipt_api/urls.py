from django.urls import path
from . import views

urlpatterns = [
    path('receipts/process', views.ReceiptsView.as_view()),
    path('receipts/<str:id>/points', views.ReceiptPoints.as_view()),
]