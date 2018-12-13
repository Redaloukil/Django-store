from django.urls import path

from store.products.views import (
    ProductsView , 
    ProductCategoryView ,
    ProductsDetailView , 
)

app_name = "users"
urlpatterns = [
    path("", view=user_list_view, name="list"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
