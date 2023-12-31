# Generated by Django 4.2.6 on 2023-11-30 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peligros', '0003_alter_peligro_url_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('clave', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=50)),
                ('Nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuario',
            },
        ),
    ]
