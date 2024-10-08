from django.shortcuts import render, redirect, reverse
from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from django.core.validators import MinValueValidator
from decimal import Decimal
import json


def delete_product(request, id):
    # Get mood based on id
    product = Product.objects.get(pk = id)
    # Delete mood
    product.delete()
    # Return to home page
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_product(request, id):
    # Get mood entry based on id
    product = Product.objects.get(pk = id)

    # Set mood entry as an instance of the form
    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Save form and return to home page
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response

   else:  
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

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

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

@login_required(login_url='/login')
def show_main(request):

    context = {
        'app_name': 'bluebird', 
        'name': request.user.username,  
        'class': 'KKI',
        'npm': '2306256425',
        'last_login': request.COOKIES['last_login'],


    }
    return render(request, 'main.html', context)


def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    else:
        messages.error(request, "Invalid username or password. Please try again.")

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    try:
        name = strip_tags(request.POST.get("name", "").strip())
        price = request.POST.get("price", "").strip()
        description = strip_tags(request.POST.get("description", "").strip())
        rating = request.POST.get("rating", "").strip()
        user = request.user

        # Validate name (non-empty)
        if not name:
            raise ValidationError('Product name is required.')

        # Validate description (non-empty, and limit length)
        if not description:
            raise ValidationError('Product description is required.')
        if len(description) > 500:
            raise ValidationError('Description must be 500 characters or fewer.')

        # Validate price (positive decimal)
        try:
            price = Decimal(price)
            MinValueValidator(Decimal('0.01'))(price)  # price must be greater than 0
        except (ValidationError, Decimal.InvalidOperation):
            raise ValidationError('Invalid price. Price must be a positive number.')

        # Validate rating (integer between 1 and 5)
        try:
            rating = int(rating)
            if not (1 <= rating <= 5):
                raise ValidationError('Rating must be between 1 and 5.')
        except ValueError:
            raise ValidationError('Invalid rating. It must be an integer between 1 and 5.')

        # Create and save the new product
        new_product = Product(
            user=user,
            name=name,
            price=price,
            description=description,
            rating=rating
        )
        new_product.save()

        return JsonResponse({'message': 'Product created successfully.'}, status=201)

    except ValidationError as e:
        # Return the specific validation error message
        return JsonResponse({'error': str(e)}, status=400)

    except Exception as e:
        # Return a generic error message for any other exceptions
        return JsonResponse({'error': 'An unexpected error occurred: ' + str(e)}, status=500)