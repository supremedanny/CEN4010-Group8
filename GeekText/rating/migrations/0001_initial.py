# Generated by Django 4.0.3 on 2022-04-13 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import isbn_field.fields
import isbn_field.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', isbn_field.fields.ISBNField(max_length=28, validators=[isbn_field.validators.ISBNValidator], verbose_name='ISBN')),
                ('ratingnum', models.FloatField(max_length=3)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
