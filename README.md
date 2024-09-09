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
'''from django.urls import path, include
urlpatterns = [
    path('', include('main.urls')),
]'''



Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.
Explain the use of git in software development!
In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?
Why is the Django model called an ORM?
