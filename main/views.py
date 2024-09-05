from django.shortcuts import render

def product_detail(request):
    context = {
        'name': 'Example Product',
        'price': 99,
        'description': 'This is a great product that you will love!',
        'rating': 4.5,
        'date': '2024-09-06'
    }
    return render(request, 'main.html', context)

# This is the index view that renders the 'main.html' template
def index(request):
    return render(request, 'main.html')  # Adjust the template name to 'main.html'

