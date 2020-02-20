# Generated by Django 2.2 on 2020-02-18 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='lst login')),
                ('cc', models.IntegerField(verbose_name='cc')),
                ('age', models.IntegerField(verbose_name='age')),
                ('univ', models.CharField(max_length=60, verbose_name='univ')),
                ('faculty', models.CharField(max_length=30, verbose_name='faculty')),
                ('gender', models.CharField(max_length=10, verbose_name='gender')),
                ('level', models.PositiveSmallIntegerField(verbose_name='age')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_U', models.BooleanField(default=False)),
                ('is_S', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
