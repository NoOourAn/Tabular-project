# Generated by Django 3.0.3 on 2020-02-14 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Email',
            field=models.CharField(max_length=255),
        ),
    ]
