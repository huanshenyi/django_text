# Generated by Django 2.1.5 on 2019-02-26 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
