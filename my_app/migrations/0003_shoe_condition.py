# Generated by Django 4.2.16 on 2024-09-11 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_shoe_brand_alter_shoe_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='condition',
            field=models.CharField(choices=[('1', 'Deadstock'), ('2', 'VNDS'), ('3', 'NDS'), ('4', 'Used'), ('5', 'Very Used')], default=1),
            preserve_default=False,
        ),
    ]
