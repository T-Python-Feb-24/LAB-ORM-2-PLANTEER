# Generated by Django 5.0.3 on 2024-03-28 02:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_rename_text_comment_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 28, 5, 38, 37, 956088)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 28, 5, 38, 37, 956088)),
        ),
    ]
