# Generated by Django 4.2.4 on 2023-11-14 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destino', '0002_myroutes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myroutes',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]