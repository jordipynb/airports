# Generated by Django 4.0.5 on 2022-06-28 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id_role',
            field=models.IntegerField(default=0, verbose_name='id'),
        ),
    ]
