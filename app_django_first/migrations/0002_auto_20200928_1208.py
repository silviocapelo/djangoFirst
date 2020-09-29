# Generated by Django 3.1 on 2020-09-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_django_first', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='data_nascimento',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='habilitado',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='idade',
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]