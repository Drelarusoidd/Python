# Generated by Django 3.2.8 on 2021-12-14 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0002_auto_20211207_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='entrance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='house',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=256),
        ),
    ]
