from django.urls import path
from .views import *

urlpatterns = [
    path('em01/', em01APIView.as_view(), name='em01'),
    path('aa06/', aa06APIView.as_view(), name='aa06'),
    path('aa22/', aa22APIView.as_view(), name='aa22'),
    path('ab01/', ab01APIView.as_view(), name='ab01'),
    path('ab09/', ab09APIView.as_view(), name='ab09'),
    path('ad01/', ad01APIView.as_view(), name='ad01'),
    path('az06/', az06APIView.as_view(), name='az06'),
]
