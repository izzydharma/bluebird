made-izzy-bluebird.pbp.cs.ui.ac.id
Step-by-Step Implementation:
1. Create a new Django project:

Use the command django-admin startproject bluebird to create a new project.
This initializes the necessary files for a Django project, including settings.py and urls.py.

2. Create an application named "main":

Inside the project directory, run python manage.py startapp main to create the application.
This adds files like views.py, models.py, and urls.py for handling the logic of the app.

3. Perform routing for the "main" app:

In the project’s urls.py, include the routing for the main application by adding

'''
from django.urls import path, include
urlpatterns = [
    path('', include('main.urls')),
]
'''

4. Create a Product model in models.py:

Define a model in main/models.py

'''
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)  
    date = models.IntegerField()  

    def __str__(self):
        return self.name
'''
Run python manage.py makemigrations and python manage.py migrate to apply the database changes.

5. Create a view to display your name and class:

'''
In views.py, define a functio
from django.shortcuts import render
def show_main(request):
    context = {
        'app_name': 'main', 
        'your_name': 'Made Izzy Prema Dharma',  
        'your_class': 'KKI'  
    }
    return render(request, 'main.html', context)
'''

6. Create routing for the about view:

In urls.py of the main app

'''
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
'''

7. Configuring the project URL Routing

Open the urls.py inisde your project directory
Add the following URL route to direct to the main view within the urlpatterns variable.

'''
    path('admin/', admin.site.urls),
    path('', include('main.urls')), 

'''
8. Deplyoing to PWS

Access the PWS page at https://pbp.cs.ui.ac.id.
Login into your account
Create a new project
Store your credentials for the project somewhere safe
On you settings.py in the project directory, add the PWS deployment URL to the allowed host
'''

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "<Your PWS deployment URL>"]

'''
Run the project command instruction that is in the PWS project page

The Diagram

Client -> Request -> urls.py -> views.py -> models.py -> HTML template -> Response -> Client


Git is used for version control, allowing developers to track changes, collaborate with others, and manage code history. It supports branching, which helps in working on new features without affecting the main codebase, and merging for integrating those features.


Django is beginner-friendly, providing clear structure and built-in features like the ORM and admin panel. Its philosophy of "batteries included" allows students to quickly grasp how web development works with less setup, while still being flexible enough to handle complex projects.Why is the Django model called an ORM?

ORM (Object-Relational Mapping) translates database queries into Python code, allowing developers to interact with the database using Python objects. Django’s ORM simplifies the management of database operations, ensuring database-agnostic code.
