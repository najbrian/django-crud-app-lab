# Generated by Django 4.2.16 on 2024-09-13 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_alter_shoe_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
