# Generated by Django 4.2.4 on 2023-12-14 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_profesional_biografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='estado',
            field=models.CharField(default='Pendiente', max_length=50),
        ),
        migrations.AlterField(
            model_name='cita',
            name='resumen',
            field=models.TextField(blank=True, null=True),
        ),
    ]
