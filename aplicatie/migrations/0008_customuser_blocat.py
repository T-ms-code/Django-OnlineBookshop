# Generated by Django 5.1.1 on 2025-01-05 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie', '0007_alter_customuser_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='blocat',
            field=models.BooleanField(default=False),
        ),
    ]
