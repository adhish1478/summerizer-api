from django.urls import path
from .views import SummarizeText

urlpatterns=[
    path('summarize', SummarizeText.as_view(), name='summarize_text'),
]