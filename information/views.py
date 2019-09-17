from django.http import JsonResponse
from django.views.generic import View

from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import serializers
from .models import (
    CompanyCode, EM01,
    AA22, AA06, AB01,
    AB09, AD01, AZ06
    )

from .serializers import (
    CompanyCodeSerializer,
    EM01Serializer,
    AA06Serializer,
    AA22Serializer,
    AB01Serializer,
    AB09Serializer,
    AD01Serializer,
    AZ06Serializer,
)

from utils.paginations import StandardResultPagination
# Create your views here.

class CompanyCodeAPIView(generics.ListAPIView):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyCodeSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = CompanyCode.objects.all().order_by('com_code')
        com_code_by = self.request.GET.get('com_code')
        mkt_by = self.request.GET.get('market_code')
        if com_code_by:
            queryset = queryset.filter(com_code=com_code_by)
        if mkt_by:
            queryset = queryset.filter(market_code=mkt_by)
        return queryset

class EM01APIView(generics.ListAPIView):
    queryset = EM01.objects.all()
    serializer_class = EM01Serializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = EM01.objects.all().order_by('-id')
        com_code_by = self.request.GET.get('com_code')
        com_status_by = self.request.GET.get('com_status')
        com_id_by = self.request.GET.get('com_identify')
        com_size_by = self.request.GET.get('com_size')
        issue_by = self.request.GET.get('issues_admin')
        ext_audit_by = self.request.GET.get('ext_audit')
        com_exist_by = self.request.GET.get('com_exist')
        fin_div_by = self.request.GET.get('fin_div')
        closure_status_by = self.request.GET.get('closure_status')
        if com_code_by:
            queryset = queryset.filter(com_code=com_code_by)
        if com_id_by:
            queryset = queryset.filter(com_identify=com_id_by)
        if com_size_by:
            queryset = queryset.filter(com_size=com_size_by)
        if com_status_by:
            queryset = queryset.filter(com_status=com_status_by)
        if issue_by:
            queryset = queryset.filter(issues_admin=issue_by)
        if ext_audit_by:
            queryset = queryset.filter(ext_audit=ext_audit)
        if com_exist_by:
            queryset = queryset.filter(com_exist=com_exist_by)
        if fin_div_by:
            queryset = queryset.filter(fin_div=fin_div_by)
        if closure_status_by:
            queryset = queryset.filter(closure_status=closure_status_by)
        return queryset


class AA06APIView(generics.ListAPIView):
    queryset = AA06.objects.all()
    serializer_class = AA06Serializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = AA06.objects.all().order_by('-id')
        date_by = self.request.GET.get('date')
        com_code_by = self.request.GET.get('com_code')
        stock_type_by = self.request.GET.get('stock_type')
        settlement_by = self.request.GET.get('settlement')
        if date_by:
            queryset = queryset.filter(date=date_by)
        if com_code_by:
            queryset = queryset.filter(com_code=com_code_by)
        if stock_type_by:
            queryset = queryset.filter(stock_type=stock_type_by)
        if settlement_by:
            queryset = queryset.filter(settlement=settlement_by)
        return queryset

class AA22APIView(generics.ListAPIView):
    queryset = AA22.objects.all()
    serializer_class = AA22Serializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = AA22.objects.all().order_by('-id')
        date_by = self.request.GET.get('date')
        com_code_by = self.request.GET.get('com_code')
        settlement_by = self.request.GET.get('settlement')
        if date_by:
            queryset = queryset.filter(date=date_by)
        if com_code_by:
            queryset = queryset.filter(com_code=com_code_by)
        if settlement_by:
            queryset = queryset.filter(settlement=settlement_by)
        return queryset

class AB01APIView(generics.ListAPIView):
    queryset = AB01.objects.all()
    serializer_class = AB01Serializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = AB01.objects.all().order_by('-id')
        date_by = self.request.GET.get('date')
        settlement_by = self.request.GET.get('settlement')
        com_code_by = self.request.GET.get('com_code')
        rep_code_by = self.request.GET.get('rep_code')
        item_code_by = self.request.GET.get('item_code')
        if date_by:
            queryset = queryset.filter(date=date_by)
        if com_code_by:
            queryset = queryset.filter(com_code=com_code_by)
        if settlement_by:
            queryset = queryset.filter(settlement=settlement_by)
        if rep_code_by:
            queryset = queryset.filter(rep_code=rep_code_by)
        if item_code_by:
            queryset = queryset.filter(item_code=item_code_by)
        return queryset


class AB09APIView(generics.ListAPIView):
    queryset = AB09.objects.all()
    serializer_class = AB09Serializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = AB09.objects.all()
        rep_code_by = self.request.GET.get('rep_code')
        item_code_by = self.request.GET.get('item_code')
        if rep_code_by:
            queryset = queryset.filter(rep_code=rep_code_by)
        if item_code_by:
            queryset = queryset.filter(item_code=item_code_by)
        return queryset

class AD01APIView(generics.ListAPIView):
    queryset = AD01.objects.all()
    serializer_class = AD01Serializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = AD01.objects.all().order_by('-id')
        date_by = self.request.GET.get('date')
        settlement_by = self.request.GET.get('settlement')
        rep_code_by = self.request.GET.get('rep_code')
        item_code_by = self.request.GET.get('item_code')
        if date_by:
            queryset = queryset.filter(date=date_by)
        if settlement_by:
            queryset = queryset.filter(settlement=settlement_by)
        if rep_code_by:
            queryset = queryset.filter(rep_code=rep_code_by)
        if item_code_by:
            queryset = queryset.filter(item_code=item_code_by)
        return queryset

class AZ06APIView(generics.ListAPIView):
    queryset = AZ06.objects.all()
    serializer_class = AZ06Serializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = AZ06.objects.all().order_by('-id')
        date_by = self.request.GET.get('date')
        com_code_by = self.request.GET.get('com_code')
        cr_code_by = self.request.GET.get('cr_code')
        if date_by:
            queryset = queryset.filter(date=date_by)
        if com_code_by:
            queryset = queryset.filter(com_code=com_code_by)
        if cr_code_by:
            queryset = queryset.filter(cr_code=cr_code_by)
        return queryset
