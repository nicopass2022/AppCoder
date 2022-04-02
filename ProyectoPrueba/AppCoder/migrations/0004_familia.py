# Generated by Django 4.0.3 on 2022-03-29 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_entregable_delete_entregableprofesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='apellido')),
                ('dni', models.IntegerField(verbose_name='dni')),
                ('fecha_nacimiento', models.DateField(verbose_name='fecha')),
            ],
        ),
    ]
