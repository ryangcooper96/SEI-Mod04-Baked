from django.urls import path
from .views import CompanyRetrieve, CompanyCreate, CompanyDetail, ProductList, ProductDetail, LineItemList, LineItemDetail

urlpatterns = [
    # Companies
    path('companies/ret/<int:user>/', CompanyRetrieve.as_view()),
    path('companies/add/', CompanyCreate.as_view()),
    path('companies/<int:pk>/', CompanyDetail.as_view()),
    # Products
    path('product/', ProductList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
    # Line Items
    path('line_item/', LineItemList.as_view()),
    path('line_item/<int:pk>/', LineItemDetail.as_view()),

]
