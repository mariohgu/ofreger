# Generated by Django 4.2.7 on 2023-11-08 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peligros', '0002_peligro_url_pdf_alter_peligro_latitud_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peligro',
            name='url_pdf',
            field=models.FileField(blank=True, null=True, upload_to='peligros_pdfs/'),
        ),
    ]