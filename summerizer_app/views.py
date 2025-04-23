from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import SummarizeTextSerializer
import re

class SummarizeText(APIView):
    def post(self, request):
        serializer = SummarizeTextSerializer(data=request.data)

        if serializer.is_valid():
            text = serializer.validated_data['text']

            # Clean the text
            text = re.sub(r'\s+', ' ', text).strip()
            text = ' '.join(text.split())

            # Very simple summarization: first 3 sentences
            sentences = re.split(r'(?<=[.!?]) +', text)
            summary = ' '.join(sentences[:3])

            return Response({'summary': summary})
        else:
            return Response(serializer.errors, status=400)