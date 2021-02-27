from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.product_list,name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<slug:category_slug>/<slug:sub_category_slug>', views.product_list, name='product_list_by_subcategory'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]