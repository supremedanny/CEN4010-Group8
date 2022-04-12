# Generated by Django 4.0.3 on 2022-04-12 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_book_isbn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(default=None, max_length=150),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
