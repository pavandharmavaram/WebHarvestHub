from django.shortcuts import render

# Create your views here.
from .models import Contact

def contact(request):
        if request.method=='POST':
            firstname=request.POST['firstname']
            secondname=request.POST['secondname']
            email=request.POST['email']
            phone_number=request.POST['number']
            message=request.POST['text']
            
            t=Contact(firstname=firstname,secondname=secondname,email=email,phone_number=phone_number,message=message)
            t.save()
        return render(request,"contact.html")