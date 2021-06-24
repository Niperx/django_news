from django.db import models

class About(models.Model):
	title = models.CharField('Заголовок', max_length = 200)
	text = models.TextField('Текст обо мне')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Обо мне'
