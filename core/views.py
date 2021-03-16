from django.shortcuts import render
from .models import Messages, Products

# Create your views here.
def home(request):
    obj = Products.objects.all()

    if request.method=='POST':
        var = request.POST
        name = var['name']
        email = var['email']
        phone = var['phone']
        message = var['message']

        messages = Messages.objects.create(Name=name, Email=email, Phone=phone, Message=message)
    
    context = {
        'obj': obj
    }
    return render(request, 'core/index.html', context)

def product(request, pk):
    obj = Products.objects.filter(id=pk)
    context ={
        'obj': obj[0]
    }
    return render(request, 'core/product_detail.html', context)