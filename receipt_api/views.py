from rest_framework.views import APIView
from rest_framework import status, serializers
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from .serializers import ReceiptSerializer
from .receipt_points import ReceiptPointsCalc


# Create your views here.
class ReceiptsView(APIView):
    def post(self, request, format=None):
        serializer = ReceiptSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                receipt = serializer.save()
            except ValidationError as e:
                return Response(e, status=status.HTTP_400_BAD_REQUEST)
            return Response({"id": receipt.pk}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReceiptPoints(APIView):
    def get(self, request, id, format=None):
        if not ReceiptPointsCalc.does_exist(id):
            return Response({"Error": f"receipt with id {id} does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        receipt_points = ReceiptPointsCalc(id)
        return Response({"points": receipt_points.generate()}, status=status.HTTP_201_CREATED)