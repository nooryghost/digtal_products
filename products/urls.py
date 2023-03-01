from django.urls import path

from .views import ProductListView, ProductDetailView

urlpatterns = [
    path("products/", ProductListView.as_view()),
    path("products/<int:pk>/", ProductDetailView.as_view())
]
