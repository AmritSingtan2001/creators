# Generated by Django 4.0.5 on 2022-08-24 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='creators',
            name='type',
            field=models.CharField(choices=[('user', 'user'), ('admin', 'admin')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]