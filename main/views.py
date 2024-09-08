from django.shortcuts import render

def show_main(request):
    context = {
        'products': [
            {
                'name': 'USB C charger',
                'price': 5,
                'description': 'Charger with braided cable',
                'rating': 4.5,
                'date': '2024-09-06'
            },
            {
                'name': 'Laptop',
                'price': 79,
                'description': 'Great laptop for everyday use',
                'rating': 4.2,
                'date': '2024-09-05'
            },
            {
                'name': 'Computer',
                'price': 300,
                'description': 'Great computer for gaming',
                'rating': 4.8,
                'date': '2024-09-04'
            }
        ]
    }
    return render(request, 'main.html', context)
