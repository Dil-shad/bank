from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import BankDetail
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from .serializers import *
from myapp.models import BankDetail
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated



def home(request):
    return render(request,'base.html')

@api_view(['GET'])
def search_ifsc(request):
    ifsc=request.GET.get('ifsc')
    banks=BankDetail.objects.filter(ifsc=ifsc)
    serializer=BankSerializer(banks,many=True)
    return JsonResponse(serializer.data,status=200,safe=False)


@api_view(['GET'])
def search_dist(request):
    city=request.GET.get('city')
    bank=request.GET.get('bank')
    banks=BankDetail.objects.filter(city=city.upper(),bank_name=bank.upper())
    serializer=BankSerializer(banks,many=True)
    return JsonResponse(serializer.data,status=200,safe=False)

class setpagination(PageNumberPagination):
    page_size=5

class BankListSearchView(ListAPIView): 
    queryset=BankDetail.objects.all()
    serializer_class=BankSerializer
    filter_backends = (filters.SearchFilter,)
    pagination_class=setpagination
    search_fields = ['city','bank_name']
    




