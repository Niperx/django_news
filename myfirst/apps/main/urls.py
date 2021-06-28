from django.urls import path, include

from . import views

app_name = 'main'
urlpatterns = [
	path('', include('articles.urls')),
	path('about/', views.about, name = 'about'),
	path('contact-us/', views.contacts, name = 'contact-us'),
]