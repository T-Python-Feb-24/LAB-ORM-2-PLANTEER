# Generated by Django 4.2.11 on 2024-03-27 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("favorites", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="favorite", old_name="post", new_name="plant",
        ),
    ]
