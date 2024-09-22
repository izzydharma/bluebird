# BLUEBIRD
# ASSIGNMENT 2
## Link : made-izzy-bluebird.pbp.cs.ui.ac.id
## 1. Step-by-Step Implementation:
### 1. Create a new Django project:

Use the command django-admin startproject bluebird to create a new project.
This initializes the necessary files for a Django project, including settings.py and urls.py.

### 2. Create an application named "main":

Inside the project directory, run python manage.py startapp main to create the application.
This adds files like views.py, models.py, and urls.py for handling the logic of the app.

### 3. Perform routing for the "main" app:

In the project’s urls.py, include the routing for the main application by adding

```
from django.urls import path, include
urlpatterns = [
    path('', include('main.urls')),
]
```

### 4. Create a Product model in models.py:

Define the models in main/models.py
name witht a character field with the max length of 100
price with an integer field
description wih a text field
rating with a decimal field 
date with an integer field

```
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)  
    date = models.IntegerField()  

    def __str__(self):
        return self.name
```
Run python manage.py makemigrations and python manage.py migrate to apply the database changes.

### 5. make the html file
in your main directory, create a file name template and make a html file named main
in the main.html input this

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>main</title>
</head>
<body>
    <h1>{{ app_name }}</h1>
    <p>Name: {{ your_name }}</p>
    <p>Class: {{ your_class }}</p>
</body>
</html>
```

```<!DOCTYPE html>```
means that this document is a HTML5 documen
```<meta charset="UTF-8">```
means that the encoding used in this document is UTF-8
```<meta name="viewport" content="width=device-width, initial-scale=1.0">```
This meta tag ensures that the page scales properly on mobile devices by setting the viewport's width to the device's width and the zoom level to 1.0.
```
<body>
    <h1>{{ app_name }}</h1>
    <p>Name: {{ your_name }}</p>
    <p>Class: {{ your_class }}</p>
</body>
```
so this creates a header with the name {app_name}
a paragraph with your name in it
and a paragraph with your class in it

the part with {} in it will be requested to views.py

### 6. Create a view to display your name and class:
In views.py, define a function

```
from django.shortcuts import render
def show_main(request):
    context = {
        'app_name': 'bluebird', 
        'your_name': 'Made Izzy Prema Dharma',  
        'your_class': 'KKI'  
    }
    return render(request, 'main.html', context)
```

so this code snippet above is used to handle an HTTP request and returns the appropriate view
this code will pass the data from the context dictionary and it will sent to the view

### 7. Create routing for the about view:

In urls.py of the main app, writhe this code
this code 

```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

### 8. Configuring the project URL Routing

Open the urls.py inisde your project directory
Add the following URL route to direct to the main view within the urlpatterns variable.

```
    path('admin/', admin.site.urls),
    path('', include('main.urls')), 

```

### 9. Deplyoing to PWS

Access the PWS page at ```https://pbp.cs.ui.ac.id```
Login into your account
Create a new project
Store your credentials for the project somewhere safe
On you ```settings.py``` in the project directory, add the PWS deployment URL to the allowed host
```

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "<Your PWS deployment URL>"]

```

Run the project command instruction that is in the PWS project page.

## 2. The Diagram

![](image/diagram.png)

When a user makes a request, the ```urls.py``` file routes the request to a view in the ```views.py``` file, which processes the request and interacts with ```models.py``` for data. The view then uses the ```main.html``` template to format the response, which is sent back to the user's browser.


## 3. Use of Git
```Git``` is used for version control, allowing developers to track changes, collaborate with others, and manage code history. It supports branching, which helps in working on new features without affecting the main codebase, and merging for integrating those features.

## 4. Reason to use Django
Django is beginner-friendly, providing clear structure and built-in features like the ORM and admin panel. Its philosophy of "batteries included" allows students to quickly grasp how web development works with less setup, while still being flexible enough to handle complex projects.Why is the Django model called an ORM?

## 5. What is ORM?
ORM (Object-Relational Mapping) translates database queries into Python code, allowing developers to interact with the database using Python objects. Django’s ORM simplifies the management of database operations, ensuring database-agnostic code.

# ASSIGNMENT 3
## 1. Step-by-Step Implementation:

### 1. Make the input form
Create a new file called ```form.py``` in the ```main``` directory of your file. Inside put the contents as follows :
```
from django.forms import ModelForm
from main.models import Product

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "rating"]
```

Edit the ```views.py``` file in the ```main``` function. Add these import line to it:

```
...
from django.shortcuts import render, redirect   # Add import redirect at this line
from main.forms import ProductEntryForm
from main.models import Product
...
```

Next, on the same file, create a new function called ```create_product_entry``` that recives a parameter ```request```

```
def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```

On the ```views.py``` file, edit the ```show_main``` function with the following content :

```
def show_main(request):
    product_entries = Product.objects.all() # add this

    context = {
        'app_name': 'bluebird', 
        'your_name': 'Made Izzy Prema Dharma',  
        'your_class': 'KKI',
        'product_entries' : product_entries #add this

    }
    return render(request, 'main.html', context)
```

Next, open the ```urls.py``` file in the ```main``` directory and import the ```create_product_entry``` function.

```
...
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
...
```

Add the URL path to the ```urlpatterns``` variable in the ```urls.py``` file in the main directory to access the function that was imported above.

```
urlpatterns = [
    ...
    path('create-mood-entry', create_product_entry, name='create_product_entry'),
    ...
```

In the root directory, make a new directory called templates. In there, make a new file called base.html with the following codes in it

```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```

Create a new HTML file with the name create_product_entry.html in the main/templates directory. Fill it with the following code :

```
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```

Then, open ```main.html``` in the ```main/templates``` directory. in there edit the ```main.html``` file as follows :

```
{% extends 'base.html' %}
{% block content %}
<h1>{{ app_name }}</h1>
<p>Name: {{ your_name }}</p>
<p>Class: {{ your_class }}</p>
{% if not product_entries %}
<p>There are no product entry yet.</p>
{% else %}
<table>
  <tr>
    <th>Product Name</th>
    <th>Date</th>
    <th>Price</th>
    <th>Desicription</th>
    <th>Rating</th>
  </tr>

  {% comment %} This is how to display product data
  {% endcomment %} 
  {% for product_entry in product_entries %}
  <tr>
    <td>{{product_entry.name}}</td>
    <td>{{product_entry.date}}</td>
    <td>{{product_entry.price}}</td>
    <td>{{product_entry.description}}</td>
    <td>{{product_entry.rating}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_product_entry' %}">
  <button>Add New Product Entry</button>
</a>
{% endblock content %}
```
Lastly, open ```settings.py``` on your project directory, and add this to the template variable

```
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # add this
        'APP_DIRS': True,
...
```

### 2.Add 4 views to view the added objects in XML, JSON, XML by ID, and JSON by ID formats.

1. On the ```model.py``` file in the ```main``` directory, add these following codes.

```
...
import uuid
...

class Product(models.Model):
    ...
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ...
```

2. Open the ```views.py``` in the ```main``` directory and import these two things
 
```
...
from django.http import HttpResponse
from django.core import serializers
...
```

On the same file, add these lines of code functions

```
...
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
...
```
3. ###  Create URL routing for each of the views added.

Open the ```urls.py``` file in the ```main``` directory and import all of the functions we made on ```views.py``` earlier.

```
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
```

Now, add the URL path to the urlpatterns variable in the urls.py file in the main directory to access the function that was imported.

```
urlpatterns = [
    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ...
]
```

Lastly, try to run the application by running the ```python manage.py runserver``` command on your command prompt and opening the http://localhost:8000/ link on your browser.

## 2. Why do we need data delivery in implementing a platform?

Data delivery is essential in implementing a platform because it enables the transfer of information between different parts of the platform, such as client-side applications and server-side systems. This ensures that users can access up-to-date data, interact with dynamic content, and perform various actions on the platform, such as creating or modifying data. Without data delivery mechanisms, the platform would be static, lacking interactivity and real-time functionality.

## 3. Which is better, XML or JSON? Why is JSON more popular than XML?

In my opinion, JSON is generally better for most modern applications due to its simplicity, readability, and ease of use with JavaScript. JSON is more lightweight, making it ideal for web services and APIs, where reducing data size is important for speed and performance. JSON’s syntax is also easier for humans to read and write, and it integrates seamlessly with modern web technologies.

JSON is more popular than XML because:
- It has less verbose syntax.
- It’s directly supported by JavaScript, which is widely used in web development.
- It’s easier to parse and more efficient in terms of performance compared to XML.

While XML is still useful for more complex configurations and documents that require a richer structure (such as metadata), JSON is better suited for the majority of modern web applications.

## 4. What is the functional usage of the `is_valid()` method in Django forms? Why do we need this method?

The `is_valid()` method in Django forms is used to check whether the data submitted via a form is valid based on the form’s fields and the associated validation rules. It ensures that all required fields are filled, data types are correct, and custom validation logic is respected. When `is_valid()` returns `True`, the form data can be safely used. If it returns `False`, the form will contain error messages explaining what went wrong.

We need this method to ensure that invalid data doesn't get processed or stored in the database, maintaining the integrity of the application’s data.

## 5. Why do we need `csrf_token` when creating a form in Django? What could happen if we did not use `csrf_token` on a Django form? How could this be leveraged by an attacker?

The `csrf_token` is used to protect forms in Django from Cross-Site Request Forgery (CSRF) attacks. CSRF occurs when an attacker tricks a user into performing unwanted actions on a website where they are authenticated, such as submitting a form on their behalf without their consent.

If we did not use `csrf_token`, an attacker could exploit this vulnerability by crafting malicious links or forms that mimic legitimate requests. For example, they could send a forged form submission to transfer money or change user settings without the user's knowledge. By adding a `csrf_token`, Django ensures that form submissions are coming from a legitimate source.

### Screenshot from postman

1. **JSON**

![](image/json.png)

2. **XML**
   
![](image/xml.png)

3. **JSON by ID**
   
![](image/jsonid.png)

4. **XML by ID**

 ![](image/xmlid.png)


# ASSIGNMENT 4

## 1. Step-by-Step Implementation:
### Implementing register function
In ```view.py``` in the ```main``` subdirectory import these library
```
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```
Then, add the register function to the ```views.py```
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
Create a new HTML file named ```register.html``` in the ```main/templates``` directory

```
{% extends 'base.html' %} {% block meta %}
<title>Register</title>
{% endblock meta %} {% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Register" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```
Open ```urls.py``` in the ```main``` directory and import the register function

```from main.views import register```

add the url path to ```urlpatterns``` to access the imported function.

```
 urlpatterns = [
     ...
     path('register/', register, name='register'),
 ]
```

### Implementing login function

Open ```view.py``` in the ```main``` directory and add these import functions

```
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
```

Add the following ```login_user``` function to ```views.py``` 

```
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

Create a new HTML name ```login.html``` in the ```main/templates``` directory

```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```

Open ```urls.py``` in the ```main``` directory and import the login function

```from main.views import login_user```

Add the URL path to ```urlpatterns``` to access the function

```
urlpatterns = [
   ...
   path('login/', login_user, name='login'),
]
```

### Implementing logout function

Open ```views.py``` and add the ```logout``` import


```from django.contrib.auth import logout```


Add the ```logout_user``` to ```views.py```

```
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

Open ```main.html``` file in the ```main/templates``` directory and add the following code snippet after the hyperlink tag for "Add New Mood Entry."

```
...
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
...
```

Open ```urls.py``` and import the ```logout_user``` function


```from main.views import logout_user```

Add the URL path to ```urlpatterns``` to access the function you imported earlier.

```
urlpatterns = [
   ...
   path('logout/', logout_user, name='logout'),
]
```

### Restricting Access to the Main Page

Open ```views.py``` in the main subdirectory and add ```the login_required``` import.

```from django.contrib.auth.decorators import login_required```

Add the code snippet ```@login_required(login_url='/login')``` above the ```show_main``` function so that the main page can only be accessed by authenticated (logged-in) users.

```
...
@login_required(login_url='/login')
def show_main(request):
...
```

### Display logged in user details such as username and apply cookies like last login to the application's main page.

Open ```views.py``` in the ```main``` directory and add these imports

```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

In the ```login_user``` function, we will add the functionality to set a cookie named ```last_login```. Replace the code in the ```if form.is_valid()``` block with the following code

```
...
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```

In the ```show_main``` function, add the snippet ```'last_login': request.COOKIES['last_login'],``` in the context variable

```
context = {
    'name': 'Pak Bepe',
    'class': 'PBP D',
    'npm': '2306123456',
    'mood_entries': mood_entries,
    'last_login': request.COOKIES['last_login'],
}
```

Change the ```logout_user``` function to be like this

```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

Open the ```main.html``` and add this code after the logout button

```
...
<h5>Last login session: {{ last_login }}</h5>
...
```

### Connect the models Product and User

Open ```models.py``` in the main subdirectory and add the following code below the line that imports the model:

```
...
from django.contrib.auth.models import User
...
```

In the previously created ```Product``` model, add the following code:

```
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    ...
```

Reopen ```views.py``` in the main subdirectory and modify the code in the ```create_product_entry``` function as follows:

```
def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        mood_entry = form.save(commit=False)
        mood_entry.user = request.user
        mood_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
 ...
```

Change the value of ```product_entries``` and ```context``` in the function ```show_main``` as follows.

```
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)

    context = {
        ...
        'your_name': request.user.username,
        ...
    }
...
```

Save all changes and run the model migration with python ```manage.py makemigrations```.

If you encounter any errors during the model migration. Just need to select ```1```.

Run ```python manage.py migrate``` to apply the migration made in the previous step.

Lastly, open ```settings.py``` in the ```bluebird``` directory and add this impor

```
import os
```

Then, change the variable ```DEBUG``` in ```settings.py``` into this.

```
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```

## Difference between HttpResponseRedirect() and redirect()

* ```HttpResponseRedirect()``` is a class-based response that specifically handles HTTP redirection by returning a status code (302) and a new URL. It requires an explicit URL to be passed as an argument.
* ```redirect()``` is a shortcut function that internally calls ```HttpResponseRedirect()``` and simplifies the redirection process by accepting a URL, a view name, or an object. It automatically resolves the URL if a view name or object is provided.

## How the Product model is linked with User

In the ```Product``` model, we establish a relationship with Django’s built-in ```User```model by adding a ```ForeignKey``` field that links each product entry to a specific user. This is done by importing the ```User``` model from ```django.contrib.auth.models``` and adding ```user = models.ForeignKey(User, on_delete=models.CASCADE)``` to the ```Product``` model. The ForeignKey ensures that each product entry is associated with a user, and if the user is deleted, their associated product entries are also removed from the database. Additionally, when creating a new product entry in the ```views.py``` file, we use ```commit=False``` to delay saving the form so that we can assign the ```user``` field to the currently logged-in user (```request.user```). This way, each product entry is saved with a reference to the user who created it. When displaying product entries on the main page, we filter them by the logged-in user, ensuring that users only see their own entries.

## Difference Between Authentication and Authorization

* Authentication is the process of verifying the identity of a user (e.g., checking their username and password).
* Authorization determines what actions or resources the authenticated user has permission to access.

When a user logs in, Django verifies their credentials (authentication) and then associates the user with specific permissions and roles (authorization) to control access.

Django handles authentication through its built-in ```django.contrib.auth system```, which includes tools for user login, logout, password management, and more.

## How Django Remembers Logged-In Users

Django uses session cookies to remember logged-in users. When a user successfully logs in, Django creates a session for that user and sets a cookie in their browser. This cookie stores the session ID, which Django uses to identify the user in subsequent requests.








