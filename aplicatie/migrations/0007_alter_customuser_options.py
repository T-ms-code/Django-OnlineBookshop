# Generated by Django 5.1.1 on 2024-12-19 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie', '0006_remove_promotii_categorie'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': [('vizualizeaza_oferta', 'Oferte doar pentru clientii privilegiati.')]},
        ),
    ]
