# Generated by Django 3.2.4 on 2021-06-25 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_comment_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
    ]
