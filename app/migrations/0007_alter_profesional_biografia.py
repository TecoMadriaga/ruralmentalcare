# Generated by Django 4.2.4 on 2023-12-14 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_profesional_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesional',
            name='biografia',
            field=models.TextField(blank=True, null=True),
        ),
    ]
