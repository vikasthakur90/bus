# Generated by Django 3.0.6 on 2020-06-07 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('uname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
    ]
