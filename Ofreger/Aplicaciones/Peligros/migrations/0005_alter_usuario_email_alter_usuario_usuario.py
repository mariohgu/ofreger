# Generated by Django 4.2.6 on 2023-12-01 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peligros', '0004_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
