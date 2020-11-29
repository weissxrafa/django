# Generated by Django 3.1.3 on 2020-11-29 11:56

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2020, 11, 29, 11, 56, 24, 911396, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='edited',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]