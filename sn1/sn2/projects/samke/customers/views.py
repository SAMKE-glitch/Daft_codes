from django.shortcuts import render, get_object_or_404
from .models import Customer

def customer_list(request):
    """Displays a list of all customers."""
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})

def customer_detail(request, customer_id):
    """Displays orders for a specific customer."""
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, 'customers/customer_detail.html', {'customer': customer})

