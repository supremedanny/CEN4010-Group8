# Generated by Django 4.0.3 on 2022-04-13 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_genre_remove_book_genre_book_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
        migrations.AddField(
            model_name='book',
            name='ISBN',
            field=models.CharField(default=0, max_length=13),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.FloatField(default=0, max_length=3),
            preserve_default=False,
        ),
    ]