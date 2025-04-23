from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.

class SummarizeText(APIView):
    def post(self, request):
        text= request.data.get('text')
        return Response({'message' : 'Text received', 'text': text})
