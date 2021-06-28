from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.urls import reverse
from django.utils import timezone

from .models import Article
from .forms import ArticleForm

import pytz

def index(request):
	latest_articles_list = Article.objects.order_by('-pub_date')[:5]
	return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
	try:
		a = Article.objects.get(id = article_id)
	except:
		raise Http404("Статья не найдена!")

	latest_comments_list = a.comment_set.order_by('-id')[:10]

	local_timezone = pytz.timezone('UTC')

	# for c in latest_comments_list:
	# 	print(c.pub_date)
	# 	c.pub_date = c.pub_date.astimezone(local_timezone)
	# 	print(c.pub_date)

	return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})

def leave_comment(request, article_id):
	try:
		a = Article.objects.get(id = article_id)
	except:
		raise Http404("Статья не найдена!")

	a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'], pub_date = timezone.now())

	return HttpResponseRedirect(reverse('articles:detail', args = (a.id,)))

def create(request):
	error = ''
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/articles')
		else:
			error = 'Форма была неверной'

	form = ArticleForm()
	context = {
		'form': form,
		'error': error
	}
	return render(request, 'articles/create.html', context)