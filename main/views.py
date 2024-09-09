from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'main', 
        'your_name': 'Made Izzy Prema Dharma',  
        'your_class': 'KKI'  
    }
    return render(request, 'main.html', context)
