# Generated by Django 3.2.4 on 2021-06-25 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200, verbose_name='Номер')),
                ('text', models.TextField(verbose_name='Описание номера')),
            ],
            options={
                'verbose_name': 'Контакты',
            },
        ),
    ]