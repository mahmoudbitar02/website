# Generated by Django 5.0.1 on 2024-01-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_portfoilo_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoilo',
            name='subtitle',
            field=models.TextField(default='', max_length=10000),
            preserve_default=False,
        ),
    ]