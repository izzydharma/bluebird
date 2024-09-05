from django.shortcuts import render

def product_detail(request):
    context = {
        'name': 'Example Product',
        'price': 99,
        'description': 'This is a great product that you will love!',
        'rating': 4.5,
        'date': '2024-09-06'
    }
    return render(request, 'main/product.html', context)

