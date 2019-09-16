from django.urls import path
from .views import *

urlpatterns = [
    path('company_code/', CompanyCodeAPIView.as_view(), name='compnay_code'),
    path('em01/', EM01APIView.as_view(), name='em01'),
    path('aa06/', AA06APIView.as_view(), name='aa06'),
    path('aa22/', AA22APIView.as_view(), name='aa22'),
    path('ab01/', AB01APIView.as_view(), name='ab01'),
    path('ab09/', AB09APIView.as_view(), name='ab09'),
    path('ad01/', AD01APIView.as_view(), name='ad01'),
    path('az06/', AZ06APIView.as_view(), name='az06'),
]
