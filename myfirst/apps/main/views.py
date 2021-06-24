from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import About

def about(request):
	info = About.objects.all()
	return render(request, 'main/about.html', {'info': info})