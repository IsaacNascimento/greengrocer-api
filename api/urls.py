from django.urls import path

from .views import views, product_views

urlpatterns = [
    path("", views.index, name="index"),
    path("get-category-list", product_views.get_category_list, name="categories"),
]