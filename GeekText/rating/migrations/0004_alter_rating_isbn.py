# Generated by Django 4.0.3 on 2022-04-13 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0003_alter_rating_ratingnum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='ISBN',
            field=models.CharField(max_length=13),
        ),
    ]
