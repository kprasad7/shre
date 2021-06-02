from django.shortcuts import render

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from vendor.models import Vendor
from details.models import Product

from vendor.forms import ProductForm
import random

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from details.models import Category, Product

def base(request):
    return render(request, 'main.html')
 

@login_required
def frontpage(request):
    newest_products = Product.objects.all()[0:8]
    return render(request, 'frontpage.html', {'kk': newest_products})



def search(request):
    query = request.GET.get('query', '')
    services = Product.objects.filter(Q( category__icontains=query) )

    return render(request, 'search.html', {'products': services, 'query': query})

def become_vendor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            vendor = Vendor.objects.create(name=user.username, created_by=user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'vendor/become_vendor.html', {'form': form})

@login_required
def vendor_admin(request):
    vendor = request.user.vendor
    products = vendor.services.all()

    return render(request, 'vendor/vendor_admin.html', {'vendor': vendor, 'products': products})


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.vendor)
            product.save()

            return redirect('vendor_admin')
    else:
        form = ProductForm()
    
    return render(request, 'vendor/add_product.html', {'form': form})

import random

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from details.models import Category, Product



def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    kk = Product.objects.all()
    similar_products = list(product.category.products.exclude(id=product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)

    return render(request, 'product.html', {'kk':kk,'product': product, 'similar_products': similar_products})

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'category.html', {'category': category})    