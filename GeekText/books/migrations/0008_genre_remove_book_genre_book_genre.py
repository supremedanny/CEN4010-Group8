# Generated by Django 4.0.3 on 2022-03-28 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_book_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(related_name='books', to='books.genre'),
        ),
    ]