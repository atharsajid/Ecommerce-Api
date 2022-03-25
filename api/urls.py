from django.urls import path
from api import views

urlpatterns = [
    path("",views.ListProductAPIView.as_view(),name="product_list"),
    path("create/", views.CreateProductAPIView.as_view(),name="product_create"),
    path("update/<int:pk>/",views.UpdateProductAPIView.as_view(),name="product_todo"),
    path("delete/<int:pk>/",views.DeleteProductAPIView.as_view(),name="product_todo")
]