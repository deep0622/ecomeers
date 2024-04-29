from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Category
from .models import Product, Customer


def index(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')

    if category_id:
        product_data = Product.objects.filter(category_id=category_id)
    else:
        product_data = Product.objects.all()

    data = {
        'productData': product_data,
        'categories': categories
    }
    return render(request, 'index.html', data)


def Signup(request):
    if request.method == 'GET':
        return render(request, 'Signup.html')

    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        value ={
            'first_name' : first_name,
            'last_name' : last_name,
            'phone' : phone,
            'email' : email

        }



        error_massage = None
        if (not first_name) :
            error_massage = "First Name requierd !!"
        elif len(first_name) < 4:
            error_massage = "First Name  must be 3 char long or more"
        elif not last_name :
            error_massage = "Last Name requierd !!"
        elif len(last_name) < 4:
            error_massage = "Last Name  must be 3 char long or more"
        elif not phone:
            error_massage = "Phone number requierd !!"
        elif len(phone) < 10:
            error_massage = "Phone number  must be 10 char long or more"
        elif len(password) < 6:
            error_massage = "Password  must be 6 char long or more"
        elif len(email) < 5:
            error_massage = "Email  must be 5 char long or more"

        if not error_massage:
            print(first_name, last_name, phone, email, password)
            customer = Customer(first_name=first_name,
                                last_name=last_name,
                                phone=phone,
                                email=email,
                                password=password)
            customer.ragister()
            return redirect('homepage')
        else:
            data = {
                'error': error_massage,
                'values' : value
            }
            return render(request, 'Signup.html',data)
