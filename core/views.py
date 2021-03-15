from django.shortcuts import render
from .models import Messages

# Create your views here.
def home(request):
    if request.method=='POST':
        var = request.POST
        name = var['name']
        email = var['email']
        phone = var['phone']
        message = var['message']

        messages = Messages.objects.create(Name=name, Email=email, Phone=phone, Message=message)
    
    return render(request, 'core/index.html')