# Generated by Django 4.0.3 on 2022-03-29 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_rename_entregableprofesor_entregable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='fecha_nacimiento',
            field=models.CharField(max_length=50, verbose_name='fecha_nacimiento'),
        ),
    ]
