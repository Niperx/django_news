from django.db import models

class About(models.Model):
	title = models.CharField('Заголовок', max_length = 200)
	text = models.TextField('Текст обо мне')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Обо мне'
		verbose_name_plural = 'Обо мне'

class Contact(models.Model):
	number = models.CharField('Номер', max_length = 200)
	text = models.TextField('Описание номера')

	def __str__(self):
		return self.number

	class Meta:
		verbose_name = 'Контакты'
		verbose_name_plural = 'Контакты'