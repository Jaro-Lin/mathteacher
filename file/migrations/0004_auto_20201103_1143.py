# Generated by Django 3.1.2 on 2020-11-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0003_auto_20201103_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marked',
            name='grade',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='marks',
            name='grade',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
    ]