from .models import Article, Comment
from django.forms import ModelForm, TextInput, Textarea

from django.utils import timezone

class ArticleForm(ModelForm):
	class Meta:
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
				'value': timezone.now()
				}),
		}

class Comment(ModelForm):
	class Meta:
		model = Comment
		fields = ["author_name", "comment_text", 'pub_date']
		widgets = {
			"comment_text": Textarea(attrs={
				'type': 'text',
				'class': 'form-control',
				'cols': '30',
				'rows': '5',
				'style': 'background-color: black;'
				}),
			"author_name": TextInput(attrs={
				'type': 'text',
				'class': 'form-control',
				'id': 'fullname'
				}),
			"pub_date": TextInput(attrs={
				'type': 'hidden',
				'class': 'form-control',
				'value': timezone.now()
				}),
		}