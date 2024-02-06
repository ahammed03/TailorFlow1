from django.shortcuts import render, redirect
from .forms import CustomerForm,MeasurementsForm
from django.db import IntegrityError
from .models import Customer  # Import your Customer model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



@login_required
def new_customer(request):
    form = CustomerForm() 

    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)

        if form.is_valid():
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            if Customer.objects.filter(tailor=request.user).filter(phone=phone):
                form.add_error('phone','Customer with this phone already exists')
            if Customer.objects.filter(tailor=request.user).filter(email=email):
                form.add_error('email','Customer with this email already exists')
            else:
                try:
                    customer = form.save(commit=False)
                    customer.tailor = request.user
                    customer.save()
                    return redirect('/customers')
                except IntegrityError as e:
                    # Handle any potential IntegrityError that may occur during the save
                    print(e)
                    form.add_error(None, 'A database integrity error occurred.')

    return render(request, 'customers/new_customer.html', context={'form': form})


def edit_customer(request,customer_id):
    customer = Customer.objects.get(id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/customers')
    else:
        form = CustomerForm(instance=customer)
    return render(request,'customers/edit_customer.html',context={'form':form})

# queryset = Customer.objects.all()
# for obj in queryset:
#     print(obj)

@login_required
def customers(request):
    tailor = request.user
    customers = Customer.objects.filter(tailor=tailor)
    return render(request,'customers/customers.html',context={'customers':customers})

@login_required
def customer_details(request,customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
        if request.method == 'POST':
            customer.delete()
            return redirect('/customers')
        return render(request,'customers/customer_details.html',context={'customer':customer})
    except:
            return HttpResponse('customer not exist.')

@login_required
def add_measurements(request,customer_id):
    form = MeasurementsForm()
    customer = Customer.objects.get(id=customer_id)
    if request.method == "POST":
        form = MeasurementsForm(request.POST)
        if form.is_valid():
            measurements = form.save()
            return redirect('/customers')
        print('form is not valid')
    return render(request,'customers/add_measurements.html',context={'form':form,'customer':customer})
