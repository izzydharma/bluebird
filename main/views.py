from django.shortcuts import render

def show_main(request):
    context = {
        'products': [
            {
                'name': 'Example Product 1',
                'price': 99,
                'description': 'This is a great product that you will love!',
                'rating': 4.5,
                'date': '2024-09-06'
            },
            {
                'name': 'Example Product 2',
                'price': 79,
                'description': 'This product is affordable and high quality!',
                'rating': 4.2,
                'date': '2024-09-05'
            },
            {
                'name': 'Example Product 3',
                'price': 149,
                'description': 'Premium product with excellent features!',
                'rating': 4.8,
                'date': '2024-09-04'
            }
        ]
    }
    return render(request, 'main.html', context)
