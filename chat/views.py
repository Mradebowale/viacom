from django.shortcuts import render, redirect
from .forms import ContactForm, Contactform2
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

from .models import Contact
# def Contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()





def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse("Something isn't right")
    else:
        form = ContactForm()
    return render(request, 'chat/index.html', {'form': form})



def contact2(request):
    if request.method == 'POST':
        form = Contactform2(request.POST)
        if form.is_valid():
            input_name = form.cleaned_data.get("name")
            input_email = form.cleaned_data.get("email")
            input_type = form.cleaned_data.get("type")
            input_message = form.cleaned_data.get("message")

            Contact.objects.create(name=input_name, email=input_email,
                                   type=input_type, message=input_message)
            messages.success(request, "Thank you for contacting us")
            return redirect("home")
        else:
            messages.error(request, "Oops, something went wrong!!")
            return redirect("https://google.com")
        
        
    else:
        form = Contactform2()
        context = {"form": form}
        return render(request, "chat/contact.html", context)
    


def contact3(request):
    if request.method == "POST":
        input_name = request.POST.get("name")
        input_email = request.POST.get("email")
        input_type = request.POST.get("type")
        input_message = request.POST.get("message")


        if len(input_name) > 100:
            messages.error(request, "name is too long")
            return redirect("contact3")
        elif input_name == "":
            messages.error(request, "name CANNOT BE EMPTY")
            return redirect("contact3")
        elif input_type == "":
            messages.error(request, "type cannot be empty")
            return redirect("contact3")
        elif input_message == "":
            messages.error(request, "message is too long")
            return redirect("contact3")
        elif input_email =="":
            messages.error(request, "name is too long")
            return redirect("contact3")
        else:
            Contact.objects.create(name=input_name, email=input_email, type=input_type, message=input_message)
            messages.success(request, "Thank you for contacting us")
            return redirect("contact")
    else:
        return render(request, "chat/contact3.html")

    