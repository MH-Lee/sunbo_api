from django.http import JsonResponse
from django.views.generic import View

from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import serializers
from .models import (
    em01, aa22, aa06,
    ab01, ab09, ad01,
    az06,
    )

from .serializers import (
    em01Serializer,
    aa06Serializer,
    aa22Serializer,
    ab01Serializer,
    ab09Serializer,
    ad01Serializer,
    az06Serializer,
)

from utils.paginations import StandardResultPagination
# Create your views here.


class em01APIView(generics.ListAPIView):
    queryset = em01.objects.all()
    serializer_class = em01Serializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = em01.objects.all().order_by('-id')
        com_code_by = self.request.GET.get('com_code')
        com_status_by = self.request.GET.get('com_status')
        com_id_by = self.request.GET.get('com_identify')
        com_size_by = self.request.GET.get('com_size')
        mkt_by = self.request.GET.get('market_code')
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
        if mkt_by:
            queryset = queryset.filter(market_code=mkt_by)
        if ext_audit_by:
            queryset = queryset.filter(ext_audit=ext_audit)
        if com_exist_by:
            queryset = queryset.filter(com_exist=com_exist_by)
        if fin_div_by:
            queryset = queryset.filter(fin_div=fin_div_by)
        if closure_status_by:
            queryset = queryset.filter(closure_status=closure_status_by)
        return queryset


class aa06APIView(generics.ListAPIView):
    queryset = aa06.objects.all()
    serializer_class = aa06Serializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = aa06.objects.all().order_by('-id')
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


class aa22APIView(generics.ListAPIView):
    queryset = aa22.objects.all()
    serializer_class = aa22Serializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = aa22.objects.all().order_by('-id')
        date_by = self.request.GET.get('date')
        com_code_by = self.request.GET.get('com_code')
        settlement_by = self.request.GET.get('settlement')
        if date_by:
            queryset = queryset.filter(date=date_by)
        if com_code_by:
            queryset = queryset.filter(com_code=com_code_by)
        if settlement_by:
            queryset = queryset.filter(settlement=settlement_by)


class ab01APIView(generics.ListAPIView):
    queryset = ab01.objects.all()
    serializer_class = ab01Serializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = ab01.objects.all().order_by('-id')
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

class ab09APIView(generics.ListAPIView):
    queryset = ab09.objects.all()
    serializer_class = ab09Serializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = ab09.objects.all().order_by('-id')
        rep_code_by = self.request.GET.get('rep_code')
        item_code_by = self.request.GET.get('item_code')
        if rep_code_by:
            queryset = queryset.filter(rep_code=rep_code_by)
        if item_code_by:
            queryset = queryset.filter(item_code=item_code_by)


class ad01APIView(generics.ListAPIView):
    queryset = ad01.objects.all()
    serializer_class = ad01Serializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = ad01.objects.all().order_by('-id')
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


class az06APIView(generics.ListAPIView):
    queryset = az06.objects.all()
    serializer_class = az06Serializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = az06.objects.all().order_by('-id')
        date_by = self.request.GET.get('date')
        com_code_by = self.request.GET.get('com_code')
        cr_code_by = self.request.GET.get('cr_code')
        if date_by:
            queryset = queryset.filter(date=date_by)
        if com_code_by:
            queryset = queryset.filter(com_code=com_code_by)
        if cr_code_by:
            queryset = queryset.filter(cr_code=cr_code_by)
