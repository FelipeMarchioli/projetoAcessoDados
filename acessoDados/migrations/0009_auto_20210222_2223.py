# Generated by Django 3.0.8 on 2021-02-23 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acessoDados', '0008_auto_20210222_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados',
            name='cpf',
            field=models.CharField(max_length=11),
        ),
    ]
