# Generated by Django 4.0.3 on 2022-04-12 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_book_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
    ]
