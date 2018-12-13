from django.shortcuts import render 
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Product


#PRODUCTS LIST 
class ProductsView(View):
    template_name = 'products.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        return render(request, self.template_name , {"products" : products})

#PRODUCTS CATEGORY LIST
class ProductCategoryView(View):
    template_name = 'products.html'
    
    def get(self, request, *args, **kwargs):
        products = get_list_or_404(Product , category=category)
        return render(request, self.template_name , {"products" : products})

#PRODUCT DETAIL
class ProductsDetailView(View):
    template_name = 'product-detail.html'

    def get(self, request, id , *args, **kwargs):
        product = get_object_or_404(Product , id)
        return render(request, self.template_name , {"product" : product})