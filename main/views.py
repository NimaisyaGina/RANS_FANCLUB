from django.shortcuts import render
from .models import Product

def show_main(request):
    products = Product.objects.all()
    context = {
        'app_name' : 'Rans Fan Club',
        'nama': 'Nimaisya Gina Herapati',
        'kelas': 'PBP C',
        'products': products,
    }

    return render(request, "main.html", context)

# Create your views here.
