from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import About, Contact

def about(request):
	info = About.objects.get(id = 1)
	return render(request, 'main/about.html', {'info': info})

def contacts(request):
	info = Contact.objects.get(id = 1)
	return render(request, 'main/contacts.html', {'info': info})