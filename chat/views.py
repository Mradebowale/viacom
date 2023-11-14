from django.shortcuts import render, redirect
from .forms import ContactForm, Contactform2
from django.http import HttpResponse
# Create your views here.


# def Contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()





def Contact(request):
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
        form = ContactForm(request.POST)
        if form.is_valid():
            input_name = form.cleaned_data.get("name")
            input_email = form.cleaned_data.get("email")
            input_type = form.cleaned_data.get("type")
            input_message = form.cleaned_data.get("message")

            Contact.objects.create(input_name, email=input_email,
                                   type=input_type, message=input_message)
            return redirect("home")
        
        else:
            form = Contactform2()
            context = {"form": form}
            return render(request, "chat/contact.html", context)