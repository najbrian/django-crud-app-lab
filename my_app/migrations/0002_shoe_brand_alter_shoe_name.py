# Generated by Django 4.2.16 on 2024-09-11 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='brand',
            field=models.CharField(default='Nike', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shoe',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]