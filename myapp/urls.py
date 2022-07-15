from django.urls import path
from .import views
from .views import (BankListSearchView)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('search_ifsc',views.search_ifsc,name='search_ifsc'),
    path('searchDist',views.search_dist,name='search_dist'),
    path('BankListSearchView',BankListSearchView.as_view(),name='BankListSearchView'),
  
    
]
