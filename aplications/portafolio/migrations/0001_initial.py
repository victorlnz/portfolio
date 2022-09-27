# Generated by Django 4.1.1 on 2022-09-23 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo:')),
                ('descripcion', models.CharField(max_length=250, verbose_name='Descripcion:')),
                ('imagen', models.ImageField(upload_to='imagen-proyectos', verbose_name='Imagen:')),
                ('url', models.URLField(verbose_name='URL:')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
    ]