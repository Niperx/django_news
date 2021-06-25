from .models import Article
from django.forms import ModelForm, TextInput, Textarea

from django.utils import timezone

class ArticleForm(ModelForm):
	class Meta:
		d = timezone.now()
		model = Article
		fields = ["article_title", "article_text", 'pub_date']
		widgets = {
			"article_title": TextInput(attrs={
				'type': 'text',
				'class': 'form-control',
				'placeholder': 'Введите название'
				}),
			"article_text": Textarea(attrs={
				'type': 'text',
				'class': 'form-control',
				'placeholder': 'Введите текст'
				}),
			"pub_date": TextInput(attrs={
				'type': 'hidden',
				'class': 'form-control',
				'value': d.strftime("%Y-%m-%d %H:%M:%S")
				}),
		}