# Generated by Django 4.0.3 on 2022-04-12 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_delete_genre_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=150, null=True),
        ),
    ]