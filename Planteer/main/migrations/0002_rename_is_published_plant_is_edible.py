# Generated by Django 5.0.3 on 2024-03-24 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='is_published',
            new_name='is_edible',
        ),
    ]
