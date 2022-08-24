# Generated by Django 4.0.5 on 2022-08-24 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150, null=True)),
                ('password', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]