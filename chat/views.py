from django.shortcuts import render, redirect
from .forms import ContactForm
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