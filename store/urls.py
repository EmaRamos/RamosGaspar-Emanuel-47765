from django.urls import path
from .views import *

urlpatterns = [

    # CRUD Products
    path('', ProductsList.as_view(), name= 'Home'),
    path('products/<int:pk>', ProductsDetail.as_view(), name= 'Products'),
    path('products/create/', ProductsCreate.as_view(), name= 'ProductsCreate'),
    path('products/update/<int:pk>', ProductsUpdate.as_view(), name= 'ProductsUpdate'),
    path('products/delete/<int:pk>', ProductsDelete.as_view(), name= 'ProductsDelete'),

    path('checkout/', checkout, name= 'Checkout'),
    path('about/', about, name= 'About')
]