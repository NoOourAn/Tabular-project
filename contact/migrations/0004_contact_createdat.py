# Generated by Django 3.0.3 on 2020-02-20 15:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_remove_contact_createdat'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='CreatedAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
