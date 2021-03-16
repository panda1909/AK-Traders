from django.urls import path
from .views import home, product, list_product, getquote

urlpatterns = [
    path('', home, name='home'),
    path('products', list_product, name='products'),
    path('quote', getquote, name='quote'),
    path('detail-product/<int:pk>/', product, name='detail-product'),
]
