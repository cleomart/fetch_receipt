from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ReceiptSerializer
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ValidationError


# create a serializer
class ReceiptsSerializer(serializers.Serializer):
    # initialize fields
    json_data = serializers.JSONField()

# Create your views here.
class ReceiptsView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer = ReceiptSerializer(data=request.data)
        print(f"serializer: {serializer}")
        if serializer.is_valid(raise_exception=True):
            try:
                receipt = serializer.save()
            except ValidationError as e:
                print(e)
                return Response(e, status=status.HTTP_400_BAD_REQUEST)
            return Response({"id": receipt.pk}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ReceiptPoints(APIView):
    def get(self, request, id, format=None):
        print("id ", id)
        return Response({}, status=status.HTTP_201_CREATED)