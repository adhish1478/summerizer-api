from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import SummarizeTextSerializer


# Create your views here.

class SummarizeText(APIView):
    def post(self, request):
        serializer= SummarizeTextSerializer(data= request.data)

        if serializer.is_valid():
            text= serializer.validated_data['text']
            import re
            text= re.sub(r'\s+', ' ', text).strip() # remove special characters
            text= ' '.join(text.split()) # remove spcaes
            #Summary logic
            sentences = re.split(r'(?<=[.!?]) +', text)
            summary= ' '.join(sentences[:3]) # taking first 3 sentences as summary
            return Response({'summary': summary})
        else:
            return Response(serializer.errors, status=400)
