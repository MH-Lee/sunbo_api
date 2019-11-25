from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('company_code/', CompanyCodeAPIView.as_view(), name='compnay_code'),
    path('em01/', EM01APIView.as_view(), name='em01'),
    path('em02/', EM02APIView.as_view(), name='em02'),
    path('aa06/', AA06APIView.as_view(), name='aa06'),
    path('aa06/<com_code>/', AA06DetailAPIView.as_view(), name='aa06'),
    path('aa22/', AA22APIView.as_view(), name='aa22'),
    path('aa22/<com_code>/', AA22DetailAPIView.as_view(), name='aa22'),
    path('ab09/', AB09APIView.as_view(), name='ab09'),
    path('az06/', AZ06APIView.as_view(), name='az06'),
    # path('ab01/', AB01APIView.as_view(), name='ab01'),
    # path('ad01/', AD01APIView.as_view(), name='ad01'),
    path('ab01/<com_code>/', AB01DetailAPIView.as_view(), name='ab01-detail'),
    path('ad01/<com_code>/', AD01DetailAPIView.as_view(), name='ad01-detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)